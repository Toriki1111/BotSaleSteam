# 🎮 Steam Daily Deal Bot (90%+ Off)

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-Automation-red?style=for-the-badge&logo=githubactions)
![Discord](https://img.shields.io/badge/Discord-Webhook-5865F2?style=for-the-badge&logo=discord)

Một con bot tự động quét các giao dịch giảm giá cực hời (trên 90%) từ Steam và gửi thông báo trực tiếp vào Discord mỗi ngày. Dự án sử dụng **Python**, **CheapShark API** và được triển khai hoàn toàn trên **GitHub Actions**.

## ✨ Tính năng nổi bật
- **Tự động quét deal:** Chạy tự động vào 8:00 AM (giờ Việt Nam) mỗi ngày.
- **Lọc thông minh:** Chỉ báo các game giảm giá từ 90% trở lên.
- **Sắp xếp chuyên nghiệp:** Ưu tiên các game giảm sâu nhất lên đầu danh sách.
- **Phân trang Discord:** Tự động chia nhỏ danh sách (10 deal/tin nhắn) để không vi phạm giới hạn của Discord.
- **Hỗ trợ múi giờ:** Hiển thị ngày tháng chính xác theo giờ Việt Nam (ICT).

## 🛠️ Công nghệ sử dụng
- **Ngôn ngữ:** Python 3.11
- **Thư viện:** `requests`, `pytz`, `python-dotenv`
- **Tự động hóa:** GitHub Actions (Cron Jobs)
- **Nguồn dữ liệu:** CheapShark API (Steam Store)

## 🚀 Hướng dẫn cài đặt

### 1. Chuẩn bị
1. Tạo một **Discord Webhook URL** trong server của bạn.
2. Fork hoặc Clone repository này về máy.

### 2. Cài đặt môi trường (Local)
```bash
# Cài đặt thư viện
pip install -r requirements.txt

# Tạo file .env và thêm Webhook của bạn
echo "DISCORD_WEBHOOK_URL=your_webhook_url_here" > .env

# Chạy thử
python src/main.py
