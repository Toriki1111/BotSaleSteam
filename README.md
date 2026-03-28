# 🎮 Steam Daily Deal Bot (90%+ Off)

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-Automation-red?style=for-the-badge&logo=githubactions)
![Discord](https://img.shields.io/badge/Discord-Webhook-5865F2?style=for-the-badge&logo=discord)

Bot tự động quét danh sách các trò chơi đang giảm giá cực sâu (từ 90% trở lên) trên cửa hàng Steam và gửi thông báo chi tiết vào Discord hàng ngày. Dự án được thiết kế để chạy hoàn toàn tự động trên nền tảng đám mây.

---

## ✨ Tính năng nổi bật
- **Tự động hóa 100%:** Sử dụng GitHub Actions để tự động kiểm tra deal vào mỗi sáng.
- **Lọc deal sâu:** Chỉ thông báo những game có mức giảm giá từ 90% trở lên.
- **Giao diện trực quan:** Thông báo trên Discord hiển thị đầy đủ tiêu đề, giá gốc, giá giảm và ảnh bìa của game.
- **An toàn & Bảo mật:** Sử dụng biến môi trường (Environment Variables) để bảo vệ thông tin Webhook.

---

## 🚀 Hướng dẫn cài đặt (Dành cho người mới)

Vì lý do bảo mật, các file cấu hình riêng tư (`.env`) và thư viện nặng (`.venv`) không được đưa lên GitHub. Vui lòng làm theo các bước sau để thiết lập:

### 1. Tải mã nguồn
- Nhấn nút **Code** -> **Download ZIP** ở góc trên bên phải trang này.
- Giải nén file vừa tải về máy tính của bạn.

### 2. Cài đặt Python (Nếu chưa có)
- Tải và cài đặt Python tại [python.org](https://www.python.org/).
- **Lưu ý:** Khi cài đặt, hãy tích vào ô **"Add Python to PATH"**.

### 3. Cài đặt thư viện hỗ trợ
Mở cửa sổ Terminal (hoặc Command Prompt/PowerShell) tại thư mục chứa dự án và chạy lệnh sau:
```bash
pip install -r requirements.txt

4. Cấu hình địa chỉ nhận tin (Webhook)
Trong thư mục dự án, tìm file tên là .env.example.

Đổi tên file này thành .env.

Mở file .env bằng Notepad và dán Link Webhook Discord của bạn vào sau dấu =:
DISCORD_WEBHOOK_URL=[https://discord.com/api/webhooks/your_id_here](https://discord.com/api/webhooks/your_id_here)
🏃 Cách vận hành
Chạy thủ công trên máy tính:
Mở Terminal tại thư mục dự án và gõ lệnh:
python src/main.py
Chạy tự động trên GitHub (Khuyên dùng):
Để bot tự chạy mỗi ngày mà không cần bật máy tính của bạn:

Vào mục Settings -> Secrets and variables -> Actions trên Repository của bạn.

Nhấn New repository secret.

Đặt tên (Name) là: DISCORD_WEBHOOK_URL

Dán link Webhook Discord của bạn vào ô Value.

Nhấn Add secret.

Hệ thống sẽ tự động gửi danh sách deal game vào Discord của bạn hàng ngày theo lịch trình đã định sẵn.

🛠️ Yêu cầu kỹ thuật
Python 3.9+

Thư viện: requests, python-dotenv, pytz.

Kết nối Internet ổn định.
