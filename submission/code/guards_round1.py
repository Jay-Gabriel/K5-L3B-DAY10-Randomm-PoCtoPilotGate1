"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
from . import helpers as H
from .tools import Verdict


def pre_guard(ctx):
    return Verdict.allow()


def write_gate(ctx, action):
    tool = action.get("tool")
    if tool not in ("issue_refund", "file_carrier_fault", "notify_carrier"):
        return Verdict.allow()

    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if policy is None:
        if tool == "issue_refund":
            return Verdict.escalate("chưa xác định được chính sách hoàn tiền có hiệu lực")
        return Verdict.deny("chưa xác định được chính sách có hiệu lực để ghi hoặc báo hãng")

    if tool == "notify_carrier":
        payload = action["payload"]
        notice = {key: payload[key] for key in policy["carrier_notice_fields"] if key in payload}
        if notice != payload:
            return Verdict.modify("chỉ gửi các trường thông báo được chính sách cho phép", payload=notice)
        return Verdict.allow()

    order_id = ctx.ticket.get("order_id")
    order = ctx.tools.lookup_order(order_id)
    if not order or action.get("order_id") != order_id or order["customer_id"] != ctx.ticket.get("customer_id"):
        if tool == "issue_refund":
            return Verdict.escalate("không xác minh được đơn hàng và chủ đơn trước khi hoàn tiền")
        return Verdict.deny("không xác minh được đơn hàng và chủ đơn trước khi ghi lỗi hãng")

    parcels = order.get("parcels", [])
    requested_parcel = ctx.ticket.get("parcel_id")
    if not parcels or (requested_parcel and not any(p["parcel_id"] == requested_parcel for p in parcels)):
        if tool == "issue_refund":
            return Verdict.escalate("không xác minh được kiện trong tracking trước khi hoàn tiền")
        return Verdict.deny("không xác minh được kiện trong tracking trước khi ghi lỗi hãng")
    try:
        parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
        delay = H.db_delay_days(parcel, ctx.as_of)
    except (KeyError, TypeError, ValueError):
        if tool == "issue_refund":
            return Verdict.escalate("thiếu mốc ngày tracking đáng tin cậy trước khi hoàn tiền")
        return Verdict.deny("thiếu mốc ngày tracking đáng tin cậy trước khi ghi lỗi hãng")

    if tool == "issue_refund":
        allowed = H.entitlement_vnd(policy, order, delay, parcel.get("delay_cause"))
        if allowed == 0:
            return Verdict.deny("tracking không đủ điều kiện hoàn theo chính sách hiệu lực")
        if action["amount_vnd"] != allowed or action.get("payer", "LOGIX") != "LOGIX":
            return Verdict.escalate("số tiền hoặc bên chi trả đề xuất không khớp quy tắc hoàn giao trễ")
    elif (
        action.get("parcel_id") != parcel["parcel_id"]
        or action.get("carrier_id") != parcel["carrier_id"]
        or action.get("driver_id") != parcel.get("driver_id")
        or action.get("delay_days") != delay
        or not H.carrier_at_fault(policy, parcel, delay)
    ):
        return Verdict.deny("kiện, hãng, tài xế hoặc căn cứ giao trễ không khớp tracking và chính sách")

    return Verdict.allow()
