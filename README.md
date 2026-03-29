# 🎮 Steam Sale Notification Bot (Spidey Bot)

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-Automation-red?style=for-the-badge&logo=githubactions)
![Discord](https://img.shields.io/badge/Discord-Webhook-5865F2?style=for-the-badge&logo=discord)

Bot tự động quét danh sách các trò chơi đang giảm giá trên cửa hàng Steam và gửi thông báo chi tiết vào Discord hàng ngày. Dự án được thiết kế để chạy hoàn toàn tự động trên nền tảng đám mây (Serverless), không cần treo máy cá nhân.

---

## ⚠️ Lưu ý về các tệp tin không hiển thị
Để đảm bảo tính bảo mật và tuân thủ quy trình phát triển chuyên nghiệp, một số thành phần sau đây sẽ **không xuất hiện** trên Repository này:
- **Thư mục `.venv/`:** Chứa các thư viện Python nặng. Người dùng chỉ cần cài đặt lại qua file `requirements.txt`.
- **Tệp `.env`:** Chứa thông tin nhạy cảm. Thay vì dùng tệp này, dự án sử dụng **GitHub Actions Secrets** (Két sắt bảo mật của GitHub) để lưu trữ Webhook URL.
- **Thư mục `__pycache__/`:** Các tệp tạm tự sinh của hệ thống, không cần thiết cho mã nguồn.
- **Thư mục `.git/`:** Dữ liệu nội bộ của hệ thống quản lý phiên bản, được GitHub tự động xử lý ẩn.

---

## ✨ Tính năng nổi bật
- **Tự động hóa 100%:** Sử dụng GitHub Actions để kiểm tra deal mỗi ngày.
- **Đúng giờ tuyệt đối:** Kết hợp với **Cron-job.org** để vượt qua giới hạn trễ giờ của hạ tầng GitHub Free.
- **Giao diện trực quan:** Thông báo Discord hiển thị đầy đủ tiêu đề, giá cũ, giá mới và ảnh bìa game.
- **An toàn & Bảo mật:** Sử dụng GitHub Secrets để bảo vệ thông tin Webhook và Token.

---

## 🛠️ Yêu cầu kỹ thuật
- Python 3.9+
- Thư viện: `requests`, `beautifulsoup4`, `python-dotenv`.
- Tài khoản GitHub & Webhook Discord.

---

## 🚀 Hướng dẫn cài đặt (Dành cho người mới)
### (Reg:) Tạo Discord Webhook
Để Bot có thể gửi tin nhắn vào Server của bạn:
1. Vào **Server Settings** -> **Integrations** -> **Webhooks**.
2. Nhấn **Create Webhook**, đặt tên cho Bot và chọn kênh nhận tin.
3. Nhấn **Copy Webhook URL**.
   - *Ví dụ định dạng (đã che):* `https://discord.com/api/webhooks/123456789/abcXYZ_xxxx_XXXX`

### 1. Cấu hình địa chỉ nhận tin (Webhook)
1. Trên GitHub Repository của bạn, vào mục **Settings** -> **Secrets and variables** -> **Actions**.
2. Nhấn **New repository secret**.
3. Đặt tên (Name) là: `DISCORD_WEBHOOK_URL`.
4. Dán link Webhook Discord của bạn vào ô **Value** và nhấn **Add secret**.
    `https://discord.com/api/webhooks/123456789012345678/ABCDEFG-hijklmnopqrstuvwxyz-123456789`

### 2. Tạo mã cấp quyền (Personal Access Token)
1. Vào **Profile Settings** -> **Developer Settings** -> **Personal access tokens (classic)**.
   Minh họa: `ghp_xxxD3exxxg6Hxxx9k0LxxxN3xxP5q6R7s`
3. Tạo token mới với quyền `workflow`. 
4. **Lưu ý:** Copy mã này ngay vì nó chỉ hiển thị 1 lần.

### 3. Tự động hóa với Cron-job.org
Để bot chạy đúng giờ mà không phụ thuộc vào hàng đợi của GitHub:
1. Đăng ký tại [Cron-job.org](https://cron-job.org/).
2. Tạo Job mới với URL API: `https://api.github.com/repos/TÊN_USER/TÊN_REPO/actions/workflows/daily_check.yml/dispatches`.
3. Cấu hình tại tab **Advanced**:
   - **Method:** `POST`.
   - **Headers:** - `Authorization`: `token [Mã_Access_Token_của_bạn]`
     - `Accept`: `application/vnd.github.v3+json`
   - **Body (Raw):** `{ "ref": "main" }`

---

## 🏃 Cách vận hành
- **Chạy tự động:** Hệ thống sẽ tự động kích hoạt thông qua Cron-job.org theo lịch trình bạn đã đặt.
- **Chạy thủ công:** Bạn có thể vào tab **Actions** trên GitHub và nhấn **Run workflow** để kiểm tra bot ngay lập tức.
