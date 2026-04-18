import os
from steam_api import get_top_deals
from notifier import send_to_discord
from dotenv import load_dotenv

# Nạp biến môi trường từ file .env (If running on Local)
load_dotenv()

def main():
    print("🚀 Bắt đầu quy trình quét deal Steam...")
    
    # 1. Gọi API để lấy danh sách deal
    all_deals = get_top_deals()
    
    if not all_deals:
        print("❌ Không tìm thấy deal nào hoặc lỗi API.")
        return

    # 2. Lọc các deal thực sự "hời" (Ví dụ: Giảm từ 90% trở lên)
    hot_deals = [d for d in all_deals if float(d['savings']) >= 90]
    
    # 3. KỸ THUẬT CS: Sắp xếp deal theo mức giảm giá từ cao xuống thấp
    # Game nào giảm 99% sẽ đứng đầu, 90% đứng cuối
    hot_deals.sort(key=lambda x: float(x['savings']), reverse=True)

    print(f"📊 Tìm thấy {len(hot_deals)} deal giảm từ 90% trở lên.")

    # 4. Gửi toàn bộ danh sách sang notifier.py 
    if hot_deals:
        send_to_discord(hot_deals)
        print("✅ Đã xử lý xong và gửi lệnh đến Discord.")
    else:
        print("ℹ️ Hôm nay không có deal nào đạt mốc 90%. Hẹn ngày mai!")

if __name__ == "__main__":
    main()
