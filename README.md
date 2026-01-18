# RS-Mini – Item-Based Collaborative Filtering (Python)

## 1. Mục tiêu dự án
Dự án này xây dựng một **Recommender System đơn giản** sử dụng
**Item-Based Collaborative Filtering**.

Hệ thống gợi ý sản phẩm / nội dung cho user dựa trên:
- Hành vi người dùng (số giờ xem, số lần tương tác, rating, …)
- Mối quan hệ giữa các item (item similarity)

Phù hợp cho:
- E-commerce
- Video / Movie platform
- Music / Podcast
- Learning platform

---

## 2. Ý tưởng chính

Giả sử:
- `rating` = **số giờ xem**
- User không đánh giá trực tiếp “thích / không thích”
→ đây là **Implicit Feedback**

Hệ thống sẽ trả lời câu hỏi:

> “User này nên xem sản phẩm nào tiếp theo,
> dựa trên những gì họ đã xem trước đó?”

---

## 3. Dữ liệu đầu vào

Dữ liệu dạng transaction:

| user_id | product_id | rating |
|--------|-----------|--------|
| U1 | P1 | 2 |
| U2 | P2 | 2 |
| U3 | P3 | 3 |
| U3 | P1 | 5 |
| U2 | P1 | 4 |

- `user_id`: người dùng
- `product_id`: sản phẩm / nội dung
- `rating`: mức độ tương tác (ví dụ: số giờ xem)

---

## 4. USER–ITEM MATRIX là gì?

Chuyển dữ liệu transaction sang dạng ma trận:

    P1   P2   P3

U1 2 0 0
U2 4 2 0
U3 5 0 3


Ý nghĩa:
- Mỗi hàng = 1 user
- Mỗi cột = 1 item
- Giá trị = mức độ tương tác

---

## 5. Item Similarity (Cosine Similarity)

Tính độ giống nhau giữa các item dựa trên hành vi user.

Ví dụ kết quả:

P1 – P2 = 0.596
P1 – P3 = 0.745


Diễn giải:
> Người xem P1 thường cũng xem P3 nhiều hơn P2

---

## 6. Recommendation Score là gì?

Với mỗi item chưa xem, hệ thống tính:

score(item_j) =
Σ ( similarity(item_j, item_i) × interaction(user, item_i) )


Ví dụ với user U1:
- U1 chỉ xem P1 = 2 giờ

score(P3) = similarity(P3, P1) × 2
= 0.745 × 2
= 1.49

score(P2) = 0.596 × 2
= 1.19


→ P3 được recommend trước P2

⚠️ Score **không phải số giờ xem**
→ chỉ là **điểm xếp hạng tương đối**

---

## 7. Kết quả hệ thống trả về

=== RECOMMEND FOR U1 ===
P3 1.49
P2 1.19


Diễn giải bằng ngôn ngữ sản phẩm:

> “Những người giống bạn,
> sau khi xem P1,
> thường xem P3 nhiều hơn P2.”

---


## 8. Cách chạy project

### 1️⃣ Tạo môi trường ảo
```bash
python3.10 -m venv venv
source venv/bin/activate

2️⃣ Cài thư viện

pip install -r requirements.txt

3️⃣ Chạy chương trình

python3.10 main.py

10. Ý nghĩa kinh doanh

Hệ thống giúp:

    Tăng thời gian sử dụng

    Cá nhân hóa trải nghiệm

    Gợi ý thông minh dựa trên hành vi thật

Không cần user đánh giá thủ công.
11. Hướng mở rộng

    Chuẩn hóa số giờ xem (log / normalize)

    Thêm popularity score

    Xử lý cold-start

    Chuyển sang User-Based CF

    Xây API bằng FastAPI

    Dùng matrix factorization

12. Kết luận

Đây là một Recommender System mini nhưng đúng bản chất:

    Có dữ liệu

    Có thuật toán

    Có ý nghĩa thực tế

    Có thể mở rộng lên production

Phù hợp làm:

    Project cá nhân

    Demo cho doanh nghiệp

    Nền tảng học ML / Data / Backend


