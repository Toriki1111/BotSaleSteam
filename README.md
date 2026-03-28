# 🎮 Steam Daily Deal Bot (90%+ Off)

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-Automation-red?style=for-the-badge&logo=githubactions)
![Discord](https://img.shields.io/badge/Discord-Webhook-5865F2?style=for-the-badge&logo=discord)

Bot tự động săn các deal game Steam giảm giá cực sâu (trên 90%) và gửi thông báo trực tiếp vào Discord. Dự án chạy hoàn toàn tự động trên Cloud (GitHub Actions).

## ✨ Tính năng nổi bật
- **Tự động hóa 100%:** Chạy vào 8:00 AM (giờ Việt Nam) mỗi ngày.
- **Lọc deal chất lượng:** Chỉ thông báo các game giảm từ 90% trở lên.
- **Bảo mật tuyệt đối:** Sử dụng Environment Variables để bảo vệ Webhook URL.
- **Giao diện Discord đẹp:** Thông báo chia theo phần, có hình ảnh minh họa game.

## 🛠️ Yêu cầu hệ thống
- Python 3.9 trở lên.
- Một Discord Webhook URL.

## 🚀 Hướng dẫn cài đặt (Cho người mới)

Vì lý do bảo mật, các file cấu hình cá nhân (`.env`) và thư viện nặng (`.venv`) đã được ẩn đi. Vui lòng làm theo các bước sau để chạy bot:

### 1. Tải mã nguồn
Nhấn nút **Code** -> **Download ZIP** ở phía trên và giải nén vào thư mục trên máy bạn.

### 2. Cài đặt môi trường
Mở Terminal/PowerShell tại thư mục dự án và chạy các lệnh sau:

```bash
# 1. Tạo môi trường ảo (giúp máy sạch sẽ)
python -m venv .venv

# 2. Kích hoạt môi trường ảo
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate

# 3. Cài đặt thư viện từ danh sách phụ tùng
pip install -r requirements.txt
