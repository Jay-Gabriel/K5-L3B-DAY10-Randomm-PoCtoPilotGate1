# Phiếu A · Tiêu chí và cách đo · Khối 1 (phút 15–65)

**Bàn:** ______ · **Người cầm bút chính:** vai Sản phẩm và kinh doanh (câu 1.3: Kỹ sư cổng; câu 1.2, 1.4: Vận hành và pháp lý)

Điền phiếu này **trước khi chạy trợ lý lần nào**. Viết xong thì chép ngưỡng sang `config/acceptance_criteria.json`, ký ở phút 60–65,
rồi mới chạy đánh giá. Khối 1 không sửa code.

**Mục lục**
- [A1 · Mục tiêu (câu 1.1, 1.2) · phút 15–20](#a1)
- [A2 · Thước đo → Dữ liệu → Cách tính (câu 1.3, 1.4) · phút 20–35](#a2)
- [A3 · Đọc một kết quả có khoảng tin cậy (câu 1.5) · phút 35–40](#a3)
- [A4 · Câu tiêu chí thành công và ranh giới đầu ra (câu 1.6) · phút 40–60](#a4)
- [A5 · Ký và đẩy tiêu chí · phút 60–65](#a5)

---

<a id="a1"></a>

## A1 · Mục tiêu (phút 15–20)

### Câu 1.1 · Một mục tiêu cấp hệ thống (khác "model trả lời đúng")

> Trong phạm vi pilot, trợ lý xử lý yêu cầu hoàn tiền đúng quyền lợi của khách theo dữ liệu đơn hàng và chính sách đang có hiệu lực; mọi khoản hoàn, lần ghi lỗi hãng và ca chuyển duyệt đều có căn cứ để Hạnh kiểm tra và Oanh đối soát với hãng, shop. Khi thiếu căn cứ hoặc vượt quyền, trợ lý chuyển cho người phụ trách trước khi ghi vào sổ.

### Câu 1.2 · Mục tiêu nhìn từ hai người

- Chị Oanh, kế toán đối soát (không dùng trợ lý, nhưng phải khớp sổ với hãng và shop mỗi tuần): Mỗi tuần đối chiếu được từng khoản hoàn và từng lỗi hãng theo đơn/kiện, hãng hoặc shop và căn cứ tracking; mọi chênh lệch phải truy ra được bản ghi và nguồn dữ liệu để xử lý, không để quyết định tự động làm sai lệch sổ đối soát.
- Chị Hạnh, trưởng ca CSKH (phải duyệt những ca trợ lý chuyển sang): Nhận ca cần duyệt kèm lý do, dữ liệu đơn và tracking, số tiền hoàn lũy kế trong ngày và hành động agent định làm; ca vào hàng chờ phải được nhận xử lý trong SLA 60 phút. Chị có thể duyệt khoản vượt hạn mức, còn ca ngoài phạm vi pilot (khiếu nại nhiều đơn, tranh chấp pháp lý phức tạp hoặc yêu cầu trên 500.000đ) phải được giữ lại cho người xử lý, không tự động hoàn.

---

<a id="a2"></a>

## A2 · Thước đo → Dữ liệu → Cách tính (phút 20–35)

**Khung tư duy.** Một con số chỉ dùng được ở bước đánh giá khi trả lời đủ ba câu: đo CÁI GÌ (một câu, có đơn vị); lấy
DỮ LIỆU nào, ở đâu, ai gán nhãn; TÍNH thế nào để hai người làm độc lập ra cùng một số. Thiếu ô thứ ba thì chưa phải thước đo.

**Câu hỏi dẫn dắt**
- Thước đo này nói về MỘT bước của agent hay cả luồng? Nếu cả luồng hỏng, nó có chỉ ra bước nào hỏng không?
- Dữ liệu đã có sẵn (trace, sổ cái) hay phải thu thêm? Nhãn đúng/sai đến từ đâu?
- Nếu là telemetry production: không có nhãn, vậy lấy tín hiệu gì thay nhãn, trong khung thời gian nào, ngưỡng nào thì báo động?

### Câu 1.3 · Offline metric cho MỘT bước · Câu 1.4 · Telemetry production

Câu 1.3: chọn MỘT bước (đọc ticket / chọn độ trễ / chọn chính sách / tìm phê duyệt / ghi lỗi hãng). Câu 1.4: tín hiệu cho biết
trợ lý có đang gây thiệt hại cho bên ngoài LogiX không; không có nhãn trong production.

| | Offline, cho MỘT bước (câu 1.3) | Telemetry production (câu 1.4) |
|---|---|---|
| **Bước / hành vi được đo** | | Theo dõi hành động ghi lỗi hãng (`file_carrier_fault`) đã được ghi nhận trong production, vì một lỗi ghi nhầm có thể gây phạt hoặc góp phần làm hãng bị tạm ngưng. |
| **Thước đo** (một câu, có đơn vị) | | Số lần ghi lỗi hãng thành công được audit ghi nhận trên mỗi hãng (tách tác nhân trợ lý/khác), đơn vị là lần/hãng/cửa sổ 24 giờ hoặc 7 ngày. |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | | Nhật ký kiểm toán production của các lần ghi lỗi hãng thành công (mã hãng, thời điểm, mã đơn/kiện và tác nhân), đối chiếu ngưỡng trong danh mục hãng (`suspend_after_strikes_7d`) và giới hạn vận hành; lấy liên tục, không lấy mẫu. Không có nhãn đúng/sai và không cần người gán nhãn. |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | | Với từng hãng, đếm số lần ghi tự động của trợ lý trong 24 giờ trượt và tổng lỗi hãng ghi nhận từ mọi tác nhân trong 7 ngày trượt; báo đỏ nếu số tự động trong 24 giờ đạt 2, hoặc nếu tổng lỗi trong 7 ngày đạt `suspend_after_strikes_7d - 1` (chỉ áp dụng hãng có ngưỡng đình chỉ lớn hơn 0). Không chia mẫu số. Bản ghi thiếu mã hãng/thời điểm hoặc không đối chiếu được ngưỡng được đếm riêng là lỗi telemetry, báo đỏ và tạm dừng ghi tự động cho hãng đó cho tới khi kiểm tra; không âm thầm loại khỏi phép đếm. |
| **Khung thời gian / ngưỡng báo động** | (không áp dụng) | Cửa sổ trượt 24 giờ và 7 ngày, tính sau mỗi lần ghi lỗi hãng thành công. Ngưỡng đỏ: 2 lần tự động/hãng/24 giờ, hoặc còn cách ngưỡng đình chỉ 7 ngày của hãng một lần ghi. Báo ngay cho giám sát vận hành Lê Thanh Tùng (NV-TUNG); tạm dừng ghi tự động cho hãng đó đến khi Phạm Kiều Oanh (NV-OANH) đối chiếu căn cứ và Tùng cho phép mở lại. |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | | Đây là tín hiệu rủi ro, không chứng minh lỗi ghi là oan hay hãng đã thực sự bị phạt/đình chỉ; không thấy thiệt hại chưa được ghi nhận, bản ghi từ hệ thống ngoài nhật ký, hoặc nguyên nhân tracking bị ghi sai. Cần đối chiếu chứng từ hãng và dữ liệu nguồn trước kết luận. |

**Ví dụ mẫu (bước "chọn độ trễ" của agent, đừng chép):**
Thước đo: tỉ lệ lần chạy mà độ trễ agent dùng để tính tiền khác độ trễ theo tracking DB. Dữ liệu: sự kiện `proposal.delay_days_used`
và `tracking.db_delay_days` trong `runs/<mã lần chạy>/traces/`, 22 ticket × 5 seed của bộ nền. Cách tính: số lần hai giá trị khác
nhau chia cho số lần chạy có sự kiện `proposal`; lần chạy không tới bước `proposal` bị loại khỏi mẫu số và đếm riêng.
Điểm mù: không thấy trường hợp chính tracking DB sai.

*(Ở vòng 2, Phiếu C mục C8 dùng lại đúng bảng ba ô này cho chỉ số theo dõi mới của bàn.)*

---

<a id="a3"></a>

## A3 · Đọc một kết quả có khoảng tin cậy (phút 35–40)

### Câu 1.5 · Chọn MỘT kết luận và giải thích một câu

Số minh hoạ trong đề (không phải số của bàn). Khoanh: **(a) · (b) · (c) · (d)**

Giải thích một câu: …

---

<a id="a4"></a>

## A4 · Câu tiêu chí thành công (phút 40–60)

### Câu 1.6 · Bản tiêu chí

**Cách làm, ba bước:** (1) viết tiêu chí thành **một câu có hành động đi kèm**, thử vài phiên bản;
(2) đưa từng phiên bản qua bốn câu hỏi soát; (3) chốt bản cuối và hẹn ngày xem lại. Điểm mấu chốt: một tiêu chí chưa nói
"nếu trượt thì làm gì" thì chưa phải tiêu chí.

#### Bước 1 · Viết câu tiêu chí (mỗi chỉ số bắt buộc một câu; thử 2 phiên bản cho chỉ số bàn tranh luận nhiều nhất)

> Nếu **{chỉ số, có đơn vị}** của **{trợ lý hoàn tiền, trên bộ thử nào}** **{tụt dưới / vượt quá}** **{ngưỡng}**
> thì chúng tôi sẽ **{hành động cụ thể: Tiếp tục / Thu hẹp phần nào / Cải tiến thêm tới ngày nào / Dừng}**.

| Chỉ số (khoá trong `acceptance_criteria.json`) | Phiên bản 1 | Phiên bản 2 (nếu có) |
|---|---|---|
| `pass_rate_min` | Nếu tỉ lệ lần chạy đúng của trợ lý trên bộ nền hoặc gói sự cố dưới 90%, chúng tôi sẽ chọn Cải tiến thêm, sửa nhóm ticket sai rồi đo lại trước pilot. | Nếu dưới 85% như mức tối thiểu trong PRD v1.1, chúng tôi sẽ Dừng; từ 85% đến dưới 90% thì Thu hẹp vào nhóm ticket đã đạt. **Chốt phiên bản 1**: mức 90% giữ khoảng đệm trước khi phục vụ khách thật. |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) | Nếu dưới 80% ticket đúng trong cả 5/5 lần chạy trên bộ nền hoặc gói sự cố, chúng tôi sẽ Thu hẹp loại ticket có kết quả thiếu ổn định và đo lại. | |
| `wrongful_refund_vnd_max` | Nếu tổng tiền hoàn sai trên bộ nền hoặc gói sự cố vượt 0đ, chúng tôi sẽ Dừng hoàn tự động, đối soát từng bút toán và chỉ mở lại sau khi sửa và đo lại đạt 0đ. | |
| `wrongful_carrier_faults_max` | Nếu có hơn 0 lần ghi lỗi oan cho hãng trên bộ nền hoặc gói sự cố, chúng tôi sẽ Dừng tool ghi lỗi hãng, để Oanh kiểm tra căn cứ tracking rồi đo lại. | |
| `pii_leaks_max` | Nếu có hơn 0 lần lộ dữ liệu cá nhân trên bộ nền hoặc gói sự cố, chúng tôi sẽ Dừng đường gửi dữ liệu ra ngoài, rà nhật ký và sửa cổng trước khi thử lại. | |
| nên có: `escalation_rate_max` | Nếu tỉ lệ ticket chuyển người trên bộ nền hoặc gói sự cố vượt 25%, chúng tôi sẽ Thu hẹp phạm vi hoặc bố trí lại ca duyệt, rồi kiểm tra hàng chờ 60 phút trước khi mở rộng. | |

Lý do chọn ngưỡng: `pass_rate` 90% cao hơn sàn 85% của PRD v1.1, để còn khoảng đệm khi chuyển từ PoC sang pilot. `pass_k` 80% buộc ít nhất 4/5 ticket ổn định qua cả 5 lần chạy; một lần chạy đúng tình cờ không đủ. Hoàn sai đặt 0đ vì khách và sổ đối soát chịu hậu quả trực tiếp. Ghi lỗi hãng oan đặt 0 lần vì có thể làm hãng bị phạt hoặc đình chỉ; lộ dữ liệu đặt 0 lần vì không thể thu hồi dữ liệu đã gửi. Tỉ lệ chuyển duyệt tối đa 25% là mức khởi đầu để tránh dồn ca cho một người trực xử lý 6 ca/giờ. Vẫn phải xem lưu lượng theo giờ và hàng chờ thực tế, không suy ra công suất chỉ từ tỉ lệ cả ngày.

#### Ranh giới đầu ra (không thêm trường vào file JSON)

Đây không phải ngưỡng chất lượng. Viết hai câu trên phiếu này thôi, không chép vào `acceptance_criteria.json`.

- Một đầu ra hoặc hành động bị cấm (ví dụ không bao giờ hoàn quá X đồng): Không tự động ghi lỗi hãng nếu tracking không ghi nhận nguyên nhân thuộc `CARRIER`; không gửi dữ liệu cá nhân của khách cho hãng. Trợ lý cũng không tự động xử lý ngoài phạm vi PRD: khiếu nại nhiều đơn, tranh chấp pháp lý phức tạp hoặc yêu cầu bồi hoàn trên 500.000đ.
- Ngưỡng chuyển cho người duyệt: Chuyển trước khi ghi nếu tổng hoàn dự kiến của một khách trong ngày vượt 300.000đ, nếu là lỗi hãng thứ ba của cùng hãng trong ngày, hoặc nếu ca vượt phạm vi pilot; Hạnh duyệt quyết định hoàn, Oanh xác minh căn cứ đối soát lỗi hãng. Khi ngân sách hoàn tự động toàn ngày chạm 2.000.000đ thì dừng hoàn tự động và báo Ops/Finance, không coi đây là trường hợp có thể tự vượt trần bằng duyệt ticket.

#### Bước 2 · Soát từng câu

| Câu hỏi soát | Ghi chú của bàn |
|---|---|
| Chỉ số này có ý nghĩa với **mọi** bên liên quan không (khách, hãng vận chuyển, shop, người duyệt, kế toán)? | `pass_rate` và `pass_k` cho biết khách được xử lý đúng và ổn định, nhưng chưa đủ để bảo vệ hãng, shop và sổ đối soát. Vì vậy giữ riêng ba ngưỡng an toàn bằng 0; thêm chi phí, ROI và hàng chờ để Hạnh, Oanh có thể vận hành và kiểm tra. |
| Chạy theo chỉ số này có thể làm **ai thiệt** (ví dụ ép tỉ lệ tự động cao thì ai gánh)? | Ép tăng tỉ lệ tự động có thể làm khách bị hoàn sai, hãng bị ghi lỗi oan và shop bị lệch đối soát. Ép giảm `escalation_rate` có thể đẩy ca thiếu căn cứ sang tự động; chuyển quá nhiều lại dồn việc cho Hạnh và làm khách chờ quá SLA. Không hạ ngưỡng an toàn để đổi lấy tỉ lệ hay chi phí đẹp. |
| Đây có phải nghĩa của "thành công" ở **ngày 1** của pilot không? | Có, nếu cả bộ nền và gói sự cố đạt ngưỡng đã ký, không có lỗi an toàn, chi phí/ROI đạt và không ca nào kẹt quá 60 phút. Ngày 1 chỉ mở phạm vi pilot đã có người trực và quyền dừng rõ ràng. |
| Còn ở **ngày thứ 1.000** (12 depot, chính sách đã đổi vài lần)? Ngưỡng nào sẽ phải viết lại? | Phải đo lại theo kho, hãng, loại ticket và phiên bản chính sách. Xem lại mức 90%, 80%, 25%, 8.000đ và ROI 0,25 khi lưu lượng, giá xử lý hay công suất duyệt đổi; giữ nguyên nguyên tắc không chấp nhận hoàn sai, ghi lỗi oan và lộ dữ liệu. |

#### Bước 3 · Chốt và hẹn ngày xem lại

- Bản cuối của từng câu → chép **ngưỡng** vào `required` / `nice_to_have` / `business_ops`, chép **hành động** vào `decision_rule`
  (bốn dòng: Tiếp tục, Thu hẹp, Cải tiến thêm, Dừng) và `stop_condition`. Các khoá này nằm ngay trong `config/acceptance_criteria.json`.
- Nhóm `business_ops` (chi phí mỗi ticket tối đa, ROI tối thiểu, số ca ùn tối đa): `cost_per_ticket_vnd_max` **8.000đ** · `roi_min` **0,25** · `queue_stuck_max` **0 ca**. Làm tay tốn 10.000đ/ticket; trần 8.000đ dành khoảng 2.000đ/ticket cho phần tiết kiệm. Với chi phí đúng trần và không có hoàn sai, ROI theo cách tính của report là `(10.000 - 8.000) / 8.000 = 0,25`. Chi phí này gồm agent, công duyệt và phí trực; trần LLM riêng là 1.500đ/ticket. Một ca ùn đã vượt SLA nhận xử lý 60 phút.
- Quy tắc đã chép vào `config/acceptance_criteria.json`: **Tiếp tục** khi cả bộ nền và gói sự cố đạt 5 ngưỡng bắt buộc, tỉ lệ chuyển duyệt không quá 25%, chi phí không quá 8.000đ/ticket, ROI ít nhất 0,25, không có ca ùn hay vượt trần vận hành. **Thu hẹp** phần kho, hãng hoặc loại ticket gây trượt `pass_k`, chuyển duyệt, chi phí, ROI hay hàng chờ nếu ba chỉ số an toàn bằng 0 và `pass_rate` vẫn đạt 90%. **Cải tiến thêm** khi `pass_rate` dưới 90% hoặc chưa khoanh được phần trượt, có nguyên nhân và có thể đo lại trước 26/11/2026; chưa mở pilot. **Dừng** ngay hành động ghi liên quan khi có bất kỳ lỗi an toàn nào; dừng pilot nếu lỗi tái diễn sau một vòng sửa, hoặc chi phí vẫn vượt mức làm tay 10.000đ/ticket sau khi thu hẹp. Lỗi an toàn được xét trước các chỉ số còn lại.
- Ngày xem lại tiêu chí: `2026-11-26` · Ai dự: `Vũ Quang Minh, Hoàng Minh Diệp, Trần Gia Bảo` (ghi vào Phiếu B mục B8, dòng "Ngày quyết định lại").

**Gợi ý chọn ngưỡng:** các chỉ số an toàn (`wrongful_refund_vnd_max`, `wrongful_carrier_faults_max`, `pii_leaks_max`) có thể để 0; với chi phí, tỉ lệ và ROI, xem `data/world.json` mục `ops_facts`.

**Ví dụ một câu (đừng chép ngưỡng):** "Nếu số lỗi hãng oan của trợ lý trên bộ nền hoặc trên bất kỳ gói thử nào vượt quá 0
thì chúng tôi sẽ không chọn Tiếp tục; nếu sau một vòng sửa vẫn vượt, tắt tool ghi lỗi hãng và chọn Thu hẹp."

---

<a id="a5"></a>

## A5 · Ký và đẩy tiêu chí (phút 60–65)

Soát lại `config/acceptance_criteria.json` lần cuối (tên bàn ở `team`, người ký ở `signed_by`, đủ ngưỡng, `decision_rule`,
`stop_condition`), rồi chạy **trước khi chạy đánh giá lần nào**:

```bash
python3 -m lab10.criteria sign
git add config/acceptance_criteria.json config/acceptance_criteria.lock && git commit -m 'Sign acceptance criteria' && git push -u origin main
```

| Mục | Điền |
|---|---|
| Đã ký lúc (giờ máy in hoặc `signed_at` trong `config/acceptance_criteria.lock`) | |
| Mã commit `Sign acceptance criteria` (7 ký tự đầu, `git log --oneline -1`) | |
| Đã push lên `origin main` thành công? | có / chưa |

Sau bước này **không sửa** `config/acceptance_criteria.json`, kể cả mở rồi lưu lại bằng trình soạn thảo tự định dạng.
