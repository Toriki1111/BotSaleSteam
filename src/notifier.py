import requests
import os
from dotenv import load_dotenv
from datetime import datetime
import pytz

load_dotenv()

def send_to_discord(deals):
    # 1. Lấy Webhook URL (Ưu tiên GitHub Secrets rồi mới đến .env)
    webhook_url = os.getenv("DISCORD_WEBHOOK_URL") or os.getenv("DISCORD_WEBHOOK")
    
    if not webhook_url:
        print("Lỗi: Không tìm thấy Webhook URL!")
        return
    
    if not deals:
        print("Không có deal nào hôm nay.")
        return

    # 2. Lấy ngày hiện tại Việt Nam (ICT)
    vietnam_tz = pytz.timezone('Asia/Ho_Chi_Minh')
    now = datetime.now(vietnam_tz)
    date_str = now.strftime("%d/%m/%Y")

    # 3. Tạo danh sách Embeds (Tối đa 10 cái để tránh lỗi Discord)
    embeds = []
    for deal in deals[:10]: 
        embed = {
            "title": deal['title'],
            "url": f"https://store.steampowered.com/app/{deal['steamAppID']}",
            "color": 15158332, 
            "fields": [
                {"name": "Giá gốc", "value": f"${deal['normalPrice']}", "inline": True},
                {"name": "Giá giảm", "value": f"${deal['salePrice']}", "inline": True},
                {"name": "Mức giảm", "value": f"📉 {deal['savings']}%", "inline": True}
            ],
            "image": {"url": f"https://cdn.cloudflare.steamstatic.com/steam/apps/{deal['steamAppID']}/header.jpg"}
        }
        embeds.append(embed)

    # 4. Gom tất cả vào Payload (Chèn date_str vào đây)
    payload = {
        "content": f"📢 **BẢN TIN DEAL STEAM - NGÀY {date_str}** 📢\n@everyone Phú ơi, vào check kèo thơm hôm nay nè!",
        "embeds": embeds
    }
    
    # 5. Gửi lên Discord
    response = requests.post(webhook_url, json=payload)
    if response.status_code == 204:
        print(f"✅ Đã gửi thành công bản tin ngày {date_str}!")
    else:
        print(f"❌ Lỗi gửi Discord: {response.status_code}")