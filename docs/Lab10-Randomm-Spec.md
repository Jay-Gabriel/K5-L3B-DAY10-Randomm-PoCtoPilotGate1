# Spec làm bài Lab 10 · Randomm · L3B

Repo làm bài: [Jay-Gabriel/K5-L3B-DAY10-Randomm-PoCtoPilotGate1](https://github.com/Jay-Gabriel/K5-L3B-DAY10-Randomm-PoCtoPilotGate1). Ghi đúng tên này vào trường `team` của file tiêu chí và file nộp.

Ba người đóng vai đội LogiX-VN. Trợ lý AI đã có bản PoC, nhiệm vụ của nhóm là dùng dữ liệu mô phỏng để quyết định liệu nó đủ điều kiện chạy thử với khách thật. Đội phải trả lời được ba câu: **AI làm được gì, ai gánh hậu quả khi nó sai, và ai có quyền dừng thử nghiệm?**

| Người | Phụ trách chính | Bàn giao cho nhóm |
|---|---|---|
| **Trần Gia Bảo** | Tech / Kỹ sư cổng | Lệnh chạy, mã lần chạy, trace, cổng bảo vệ, test và monitor |
| **Vũ Quang Minh** | Sản phẩm và kinh doanh (phân công đề xuất) | Phiếu A, lý do chọn ngưỡng, bản đồ dữ liệu, chi phí/ROI, bản nháp v1 và v2 |
| **Hoàng Minh Diệp** | Vận hành và pháp lý (phân công đề xuất) | HAZOP, PIC, quyền duyệt, runbook, hồ sơ sự cố và checklist nộp |

Cả ba cùng thống nhất ngưỡng, ưu tiên rủi ro và quyết định. MSSV và trưởng nhóm điền theo thông tin thật. **Bảo đã được xác định là Tech**, hai vai còn lại có thể đổi chỗ nếu nhóm phân công khác.

## CP1 · Cài đặt và chia vai · phút 0–15

**Đầu vào** — Repo Randomm đã clone, Python 3, Git, họ tên và MSSV của ba người, một eval card và một PRD v1.1 từ Lab 9.

- **Bảo:** mở terminal ở thư mục Randomm, chạy hai lệnh dưới đây. Chuẩn bị một máy chạy chính để nhóm dùng chung mã lần chạy và báo cáo.
- **Minh:** đưa eval card và PRD đã chọn cho cả bàn. Ghi lại mục tiêu của Lab 9 và phần chưa biết về điều kiện pilot.
- **Diệp:** hoàn thành bảng `TEAM.md`, xác định trưởng nhóm, kiểm tra mỗi thành viên có quyền làm việc trên repo. Mỗi người tự viết mục cá nhân trước khi nộp, có đóng góp, bằng chứng, exit ticket và phần dùng AI nếu có.
- **Trưởng nhóm:** cấu hình danh tính Git của repo theo MSSV và email giả như đề. Xác nhận máy chạy chính có quyền push để CP2 kịp lưu mốc ký. Repo đang dùng trong spec là Randomm. Slide lớp và README có hai hướng dẫn khác nhau về cách tạo repo/nhận thẻ, nên hỏi Coach để thống nhất cách làm trước khi ký.

```bash
git remote -v
python3 -m unittest discover -s tests
```

**Đầu ra** — `TEAM.md` đủ thông tin, `origin` trỏ về repo nhóm, test hiện `Ran 13 tests` và `OK`. Đây là test cài đặt, làm được ngay ở CP1.

## CP2 · Viết và ký Acceptance Criteria · phút 15–65 · 15 điểm

**Đầu vào** — Một eval card và một PRD v1.1 chung từ Day 9, cùng đề, dữ liệu mô phỏng và mẫu JSON của Day 10.

- [PRD v1.1 Day 9 của Bảo](https://github.com/Jay-Gabriel/K5-L3B-DAY09-TranGiaBao-2A202603914-EvaluationandFailureAnalysis/blob/main/docs/PRD_v1.1.md) — Minh đọc mục 3, Diệp đọc mục 2 và 6 để điền A1.
- [Eval card Day 9 của Bảo](https://github.com/Jay-Gabriel/K5-L3B-DAY09-TranGiaBao-2A202603914-EvaluationandFailureAnalysis/blob/main/docs/eval_card.md) — cả nhóm dùng chung để tham khảo cách đo cho A2.

- **Minh:** đọc **PRD v1.1 §3** cho câu 1.1. Dùng `ops_limits` và `ops_facts` của Day 10 để giải thích các ngưỡng mới ở câu 1.6.
- **Diệp:** đọc **PRD v1.1 §2 và §6** cùng `data/world.json` mục `staff` cho câu 1.2. Thiết kế tín hiệu theo dõi và ngưỡng cảnh báo cho câu 1.4.
- **Bảo:** dùng eval card Day 9 để tham khảo cách đánh giá, rồi thiết kế chỉ số offline cho một bước của trợ lý ở câu 1.3 dựa trên dữ liệu Day 10.

| Người | Việc cụ thể | Đầu ra |
|---|---|---|
| **Minh** | Viết mục tiêu cấp hệ thống (1.1), chủ trì chốt ngưỡng và quy tắc quyết định (1.6). Giải thích ngưỡng qua tác hại, chi phí và phạm vi pilot. | A1 (1.1), A4, các ngưỡng và lý do trong bản tiêu chí |
| **Bảo** | Chọn một bước của agent và thiết kế chỉ số offline (1.3). Ghi rõ nguồn nhãn, trường cần đọc, mẫu số, xử lý ca thiếu và điểm mù. Kiểm tra các khóa JSON rồi thực hiện ký cùng trưởng nhóm. | A2 (1.3), file tiêu chí, file khóa, căn cứ ghi A5 |
| **Diệp** | Viết mục tiêu cho chị Oanh đối soát và chị Hạnh trưởng ca (1.2). Chọn một tín hiệu production quan sát được khi chưa có nhãn (1.4), gắn ngưỡng báo và người xử lý. Viết ranh giới cấm và ngưỡng chuyển người duyệt cùng Minh. | A1 (1.2), A2 (1.4), phần ranh giới trong A4 |
| **Cả nhóm** | Làm A3, soát A4 cho mọi bên liên quan, ai có thể chịu thiệt, ngày 1 và ngày 1.000. Chốt ngày xem lại, người ký và bốn phương án quyết định. | Phiếu A đủ A1–A5 |

Điền đủ trong `config/acceptance_criteria.json`:

- `required`: `pass_rate_min`, `pass_k_min`, `wrongful_refund_vnd_max`, `wrongful_carrier_faults_max`, `pii_leaks_max`.
- `nice_to_have`: `escalation_rate_max`.
- `business_ops`: `cost_per_ticket_vnd_max`, `roi_min`, `queue_stuck_max`.
- `team`, `signed_by`, `stop_condition` và bốn dòng `decision_rule`. Hai câu ranh giới hành động nằm trong Phiếu A.

**Dẫn chứng để hiểu cách viết:** Một mục tiêu cấp hệ thống có thể nói về xử lý đúng quyền lợi khách và để sổ đối soát giải thích được từng khoản hoàn. Với chỉ số offline của bước chọn chính sách, hãy so chính sách được chọn trong trace với chính sách có hiệu lực ở thời điểm giao dịch theo dữ liệu gốc. Chỉ rõ mẫu số là các lần có đủ căn cứ đối chiếu và đếm riêng các ca thiếu; chỉ số này vẫn có điểm mù nếu dữ liệu chính sách gốc sai. Đây là ví dụ về cấu trúc, nhóm cần xác minh trường thực tế và tự chọn cách tính.

**Chỗ dễ nhầm:** Nếu một ticket đúng 4/5 lần, nó đóng góp 4 lần đúng vào `pass_rate`, trượt `pass^k` (bài dùng cả 5/5), và đạt `pass@5` (ít nhất một lần). A3 dùng số minh họa đề cho. Trong bài đó, chênh một lần chạy chưa đủ kết luận bản Y tốt hơn.

Sau khi cả ba thống nhất:

```bash
python3 -m lab10.criteria sign
git add config/acceptance_criteria.json config/acceptance_criteria.lock
git commit -m "Sign acceptance criteria"
git push -u origin main
```

**Đầu ra** — Máy báo `ĐÃ KÝ.`, commit đã lên GitHub **trước lần đánh giá đầu tiên**, ghi giờ và mã commit vào A5. Từ đó giữ nguyên file tiêu chí và file khóa. Nếu push lỗi, xử lý quyền push trước khi chạy đánh giá. Các ngưỡng và quyết định do nhóm chọn và phải giải thích được.

## CP3 · Đo, tìm rủi ro, dựng cổng vòng 1 và quyết định v1 · phút 65–115 · 30 điểm

**Đầu vào** — Tiêu chí đã ký và push, bộ `base`, dữ liệu mô phỏng, Phiếu B.

### 65–85 · Đo và tìm rủi ro

| Người | Việc cụ thể | Bằng chứng bàn giao |
|---|---|---|
| **Bảo** | Chạy baseline, so tiêu chí, đọc cả bảng kho/hãng và kinh doanh/vận hành. Trace `T-002@55`, ghi triệu chứng, loại lỗi, nguồn và hướng xử lý. Nêu cả lợi và hại của việc để cổng tự chặn bản phát hành, rồi chọn tự chặn, người duyệt hoặc kết hợp. | B0–B2, mã lần chạy, dòng trace |
| **Minh** | Bản đồ dữ liệu. Mỗi trường ghi nguồn sự thật hoặc bản sao, nơi dữ liệu có thể lệch. Nêu một tình huống drift cụ thể trong ba tháng tới: ngày dự kiến, trường thay đổi, loại drift, chỉ số bị ảnh hưởng và tín hiệu phát hiện. | B3 |
| **Diệp** | HAZOP cho một tool ghi, ít nhất ba dòng trên tool và thêm ít nhất hai dòng ngoài kỹ thuật. Điền checklist chín nhóm với trạng thái, bằng chứng và PIC có tên cho từng dòng. | B4–B5 |
| **Cả nhóm** | Giả sử pilot phải dừng sau ba tháng. Tìm nguyên nhân theo bốn lăng kính kỹ thuật, kinh doanh, con người/vận hành và pháp lý. Chọn 2–3 nguyên nhân để dựng cổng ngay. | B6, mỗi lý do ưu tiên nối tới một cổng |

```bash
python3 -m lab10.eval --suite base --stage base --note "baseline"
python3 -m lab10.gate --run runs/<ma-run-base>/report.json
python3 -m lab10.trace --suite base --ticket T-002 --seed 55
```

Trong các lệnh, thay toàn bộ phần nằm trong `<…>` bằng giá trị thật trước khi chạy.

### 85–105 · Dựng cổng

- **Bảo — B7.1–B7.3.** Viết 2–3 cổng trong `lab10/guards.py`. `pre_guard` kiểm tra trước khi trợ lý đọc ticket, `write_gate` kiểm tra trước hành động ghi. Với mỗi cổng, ghi rủi ro nguồn, dữ liệu tin cậy, hành động cho qua/chặn/chuyển duyệt và ca hợp lệ phải giữ. Nêu hai bước tránh tối ưu theo dữ liệu chấm, ví dụ thiết kế quy tắc theo chính sách và tự tạo biến thể thay vì dựa vào ID hoặc câu chữ. Cùng Minh hoặc Diệp tạo hai ticket `--adhoc` để kiểm tra một tính chất và lưu kết quả cho demo.
- **Minh — B7.4.** Điền `business` trong `config/operating_gates.json`. Mỗi con số có đơn vị, căn cứ và tác động lên chi phí hoặc độ phủ. Ví dụ dữ liệu mock ghi 6 ca/giờ/người, 8 giờ/ca và 30.000đ phí giữ chỗ cho mỗi người trực thêm. Khi đề xuất tăng nhân sự, tính công suất và phí dựa trên cùng ca, rồi đối chiếu report. Phân biệt chi phí LLM với tổng chi phí mỗi ticket.
- **Diệp — B7.5–B7.6.** Điền `operations` và `legal`. Chốt PIC, người có quyền duyệt/tắt, công suất, SLA chờ, kênh báo, trường dữ liệu không gửi ra ngoài và căn cứ ghi lỗi hãng. Runbook 1–3 và giờ cao điểm phải khớp config. Ghi rõ từ tín hiệu đỏ đến khi dừng tối đa bao lâu, ai thao tác, ai nhận ticket khi tắt.
- **Phối hợp:** Minh và Diệp bàn giao các trường config cho Bảo kiểm tra chung một lượt. Mỗi người chịu trách nhiệm phần của mình để tránh ghi đè file dùng chung.

```bash
python3 -m lab10.eval --suite base --stage after --note "cong vong 1"
python3 -m lab10.trace --suite base --stage after --adhoc "<noi-dung-test>" --order <ma-don> --customer <ma-khach>
python3 -m unittest discover -s tests
```

**Ví dụ behavioral test:** Cùng một tính chất “tin nhắn khách không tự thay thế dữ liệu tracking dùng cho quyết định”. Tạo hai ticket mới bằng cách diễn đạt khác nhau. Dùng một đơn có tracking không đủ điều kiện để thử đường chặn/chuyển duyệt và một đơn thực sự đủ điều kiện để thử đường xử lý hợp lệ. Trước khi chạy, ghi trước kỳ vọng của từng ca. Chọn mã đơn/khách thật có trong dữ liệu mock, ghi lệnh và dòng kết quả; kết quả thực tế mới là bằng chứng.

### 105–115 · Chốt và quyết định v1

```bash
python3 -m lab10.checkpoint
python3 -m lab10.eval --suite base --stage prepared
python3 -m lab10.gate --run runs/<ma-run-prepared>/report.json
```

**Bảo** tạo bản chốt và bàn giao số liệu. **Minh** viết B8 với một quyết định, ba bằng chứng gắn mã lần chạy, kho/hãng xấu nhất, dòng quy tắc đã ký và ngày quyết định lại. **Diệp** đối chiếu số liệu về duyệt, hàng đợi và pháp lý. Cả nhóm chốt, commit và push theo B8 trước khi nhận thẻ. Sau mốc này giữ nguyên v1 và các file snapshot/lock.

**Đầu ra** — Phiếu B đủ B0–B8, hai ticket hiểm, bản `prepared`, v1 và lịch sử Git. Vòng 1 tốt phải có cổng giải quyết rủi ro có lý do và giữ những ticket đang xử lý đúng.

## CP4 · Nhận thẻ, phân tích và sửa · phút 125–185 · 45 điểm

**Đầu vào** — BTC cấp đúng một mã thẻ, hướng dẫn nhận thẻ của Coach, bản prepared đã chốt, cấu hình hiện có. Chỉ làm thẻ được giao.

1. **125–135. Bảo** lấy đúng thư mục thẻ theo hướng dẫn Coach và chạy lệnh grade **trước khi sửa cổng, cấu hình hay monitor**. **Diệp** ghi mã thẻ vào Phiếu C. **Minh** ghi dòng vượt trần và cổng prepared đã đỡ gì vào C0–C1. Cả nhóm so lại với pre-mortem.
2. **135–155. Bảo** trace ít nhất hai ticket hỏng theo hai kiểu khác nhau. C2 có ít nhất hai lỗi từ hai nguồn, trong đó có lỗi chìm, và ghi tác hại cho ai, bao nhiêu ở base. **Diệp** điền C3 đúng phần của thẻ, S4 được bỏ C3, và HAZOP C4 ít nhất ba dòng, có một nhánh chưa thấy trên trace khi viết. **Minh** viết một yêu cầu kiểm được cho C5, Diệp viết một giả định môi trường có thể sai. Cả ba làm C6 với ít nhất hai nhánh ở hai tầng; mỗi lá có `ticket@seed`, trường dữ liệu hoặc dòng report.
3. **155–180. Bảo** sửa cổng ở đúng tầng kỹ thuật nếu cần và thêm ít nhất một hàm monitor mới, đăng ký vào `MONITORS`. **Minh** sửa giới hạn/phạm vi khi nguyên nhân nằm ở kinh doanh. **Diệp** sửa quy trình/quyền duyệt/nhân sự khi nguyên nhân nằm ở vận hành. Mỗi thay đổi có một nhánh nguyên nhân tương ứng trong C7. C8 ghi công thức, trường trial, đơn vị, mẫu số, cách xử lý dữ liệu thiếu, ngưỡng, khung thời gian, điểm mù và giá trị thực tế. Chỉ số đọc trial chưa có nhãn và chỉ số `escalation_rate` có sẵn không tính là monitor mới.
4. **180–185. Diệp** cập nhật fault tree sau sửa, ghi nhánh còn hở, thêm ít nhất một dòng risk register có PIC/tín hiệu/hành động và cập nhật checklist/runbook 4–5 ở C9–C11. **Bảo** bàn giao mã lần chạy; **Minh** kiểm tra lại chi phí, ROI và độ phủ.

```bash
python3 -m lab10.grade --incident Sx
python3 -m lab10.trace --suite Sx --ticket <ma-ticket> --seed <seed>
python3 -m lab10.eval --suite Sx --stage after --note "<thay-doi-can-do>"
python3 -m lab10.eval --suite base --stage after --note "kiem lai bo nen"
python3 -m lab10.grade --incident Sx
```

Thay `Sx` bằng mã thẻ thật. Lệnh grade đầu là trước khi chỉnh, lệnh grade cuối là sau khi chỉnh. Với trace, xem hướng dẫn của thẻ và ghi mốc chạy tương ứng với bằng chứng muốn lấy.

**Dẫn chứng để hiểu fault tree:** Giả sử tác hại là hãng bị ghi lỗi oan. Một nhánh kỹ thuật có thể là dữ liệu dùng để ghi thiếu căn cứ. Một nhánh vận hành có thể là ca cần xác minh không tới được người có quyền xử lý. Nếu có cổng chặn ghi khi thiếu căn cứ, ghi rõ cổng ngăn được nhánh nào và giả định “nguồn tracking đủ tin cậy” còn hở ở đâu. Nếu chỉ thêm monitor, ghi mức giảm nhờ phát hiện sớm và ai xử lý cảnh báo. Dùng bằng chứng từ thẻ thật để xác nhận cây, tránh áp ví dụ vào thẻ chưa đọc.

**Đầu ra** — C0–C11, report ba mốc, mã lần chạy và trace, diff sửa hợp lệ, monitor mới. So `integrity`, `visible`, `regression` và `monitor`. Đọc chỉ số an toàn, hàng chờ, chi phí, ROI, độ phủ, từng kho/hãng và các dòng vượt trần. Test ẩn do team chấm chạy sau buổi học. Chặn hàng loạt, thu hẹp phạm vi về 0, hardcode ID hoặc thêm nhiều người chỉ để làm đẹp số đều làm mất căn cứ cho pilot và có thể mất điểm.

## CP5 · Quyết định v2, demo và nộp · phút 185–240 · 10 điểm

**Đầu vào** — Báo cáo ba mốc của thẻ, quyết định v1, tiêu chí đã ký, fault tree, dữ liệu theo kho/hãng.

- **Minh** chủ trì C12. Chọn một trong bốn quyết định, dẫn ba bằng chứng gắn mã lần chạy, tính cả kho/hãng xấu nhất và nói vì sao đổi hoặc giữ v1. Nếu thu hẹp, nêu kho nào, độ phủ còn bao nhiêu, số người trực và nơi chuyển ticket ngoài phạm vi. Nếu cải tiến thêm, nêu giả thuyết, người làm và hạn. Nếu dừng, ghi bài học. Chỉ cân nhắc **Tiếp tục** khi không còn dòng vượt trần và các ngưỡng đã ký đều đạt.
- **Diệp** kiểm tra C12 và ghi ba dòng bắt buộc: giả định môi trường có thể sai, biện pháp giảm hay ngăn tác hại và vì sao, điều cần đo lại với dữ liệu thật trước Gate 2. Chép nguyên ba dòng sang `three_lines`; điền `team`, `members` theo `HoVaTen-MSSV`, thẻ, v1, v2 trong `submission/submission.json`.
- **Bảo** chạy kiểm tra/gom bài trên code và config cuối. **Trưởng nhóm** đẩy bài và kiểm tra trên GitHub có đủ hồ sơ. **Mỗi người** hoàn thành phần cá nhân trong `TEAM.md` và tự nộp link repo lên LMS.

```bash
python3 -m lab10.grade --incident Sx
python3 -m lab10.check_submission --collect
```

**Đầu ra** — C12 và JSON khớp nhau; máy báo `ĐỦ THÀNH PHẦN`; repo có `submission/`, `TEAM.md`, bản chốt, các report và journal theo checklist. Với lớp chiều/tối, hướng dẫn ghi hạn LMS 11:59 ngày hôm sau (GMT+7), trừ khi Coach có thông báo khác. Báo đủ thành phần chỉ xác nhận hồ sơ, còn chất lượng do rubric và test ẩn đánh giá.

## Demo 5 phút · cả ba đều có phần

| Thời gian | Người | Nói và chiếu |
|---|---|---|
| 0:00–0:40 | **Minh** | Tác hại là gì, ai chịu, nhóm đã ký tiêu chí nào. Chiếu report ba cột **base → prepared → after** của **cùng thẻ**. |
| 0:40–2:00 | **Bảo** | Chiếu một trace thật. Chỉ dữ liệu đầu vào, bước sai, cổng vòng 1 đã đỡ gì, còn hở gì, và sửa vòng 2 ở đâu. Chốt bằng một số trước/sau và một điểm regression. |
| 2:00–2:50 | **Diệp** | Chỉ một nhánh ngoài code, ai duyệt hoặc dừng, monitor nào báo và tác hại được giảm hay ngăn. Nếu còn rủi ro, nói ai theo dõi và khi nào hành động. |
| 2:50–3:40 | **Minh** | Chốt v2 bằng một số an toàn, một số vận hành/chi phí và kho/hãng xấu nhất. Chỉ dòng `decision_rule` tương ứng. |
| 3:40–5:00 | **Cả nhóm** | Bàn bạn đưa ticket hiểm hoặc đề xuất đổi một con số. Bảo chạy trực tiếp, Minh đọc ảnh hưởng tiền/phạm vi, Diệp đọc ảnh hưởng tới quyền duyệt hoặc hàng chờ. |

Chuẩn bị sẵn report, trace, lệnh, mã giả đã chọn trong dữ liệu mock, và hai ticket hiểm. Nếu demo đổi config, trả lại bản v2 rồi chạy lại grade và gom bài theo đề trước khi push. Dùng số thật từ report và ghi cả hạn chế. Câu dẫn dễ nhớ khi trình bày một thay đổi: **“Ở mốc [X], [chỉ số] là [giá trị]. Vì [dòng trace/dữ liệu], nhóm đổi [cổng hoặc quy trình]. Mốc [Y] ghi [giá trị], và [rủi ro] còn cần theo dõi.”**

## Tự soát theo rubric

| Ưu tiên | Điểm | Cách tự soát |
|---|---:|---|
| Điều kiện qua | Bắt buộc | Ký và push trước đánh giá, giữ nguyên file khóa và snapshot, v2 khớp bằng chứng, lệnh gom báo đủ. |
| CP2 · C1 | 15 | Ngưỡng có căn cứ và hành động, chỉ số có công thức, đủ `business_ops` và bốn quy tắc. |
| CP3 · C2–C3 | 30 | HAZOP đủ chiều, 9 PIC có tên, cổng nối với pre-mortem, runbook khớp config, prepared và v1 có bằng chứng. |
| CP4 · C4–C5 | 45 | Report trước/sau, test hồi quy, giữ độ phủ có ích, monitor mới, fault tree có bằng chứng, risk register có hành động. |
| CP5 · C6 | 10 | V2 giải thích đổi/giữ, số liệu gắn quyết định và ba dòng cụ thể, khớp JSON. |
| Bonus | Tối đa +10 | +5 nếu prepared đã đỡ phần lớn sự cố; +5 nếu cổng hoặc monitor phát hiện lỗi chìm ngoài thẻ và có trace. |

Mỗi bằng chứng nên có **mã lần chạy hoặc commit → ticket@seed / mục report → số hoặc trường cụ thể → kết luận → mục phiếu**. Cuối mỗi checkpoint, cả ba dành một lượt đối chiếu để ai cũng hiểu phần người kia làm. Nhớ so tên repo, MSSV và mục cá nhân trước khi nộp vì các lỗi này ảnh hưởng điểm.

Nguồn: [Đề bài](https://github.com/Jay-Gabriel/K5-L3B-DAY10-Randomm-PoCtoPilotGate1/blob/main/problem-set.md) · [Rubric](https://github.com/Jay-Gabriel/K5-L3B-DAY10-Randomm-PoCtoPilotGate1/blob/main/RUBRIC.md) · [Checkpoints](https://github.com/Jay-Gabriel/K5-L3B-DAY10-Randomm-PoCtoPilotGate1/blob/main/CHECKPOINTS.md) · [Hướng dẫn nộp](https://github.com/Jay-Gabriel/K5-L3B-DAY10-Randomm-PoCtoPilotGate1/blob/main/SUBMISSION.md) · [Dữ liệu mock](https://github.com/Jay-Gabriel/K5-L3B-DAY10-Randomm-PoCtoPilotGate1/blob/main/data/world.json).
