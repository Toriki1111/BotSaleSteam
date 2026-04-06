import os
import requests
import pytz
from datetime import datetime
from dotenv import load_dotenv

# Nạp biến môi trường từ .env (cho máy local)
load_dotenv()

def send_to_discord(deals):
    # 1. Lấy Webhook URL từ GitHub Secrets hoặc .env
    webhook_url = os.getenv("DISCORD_WEBHOOK_URL") or os.getenv("DISCORD_WEBHOOK")
    
    if not webhook_url:
        print("❌ ERR: Cannot found Webhook URL in Secrets or in .env!")
        return
    
    if not deals:
        print("ℹ️ No deal today")
        return

    # 2. Lấy ngày hiện tại theo múi giờ Việt Nam (ICT)
    vietnam_tz = pytz.timezone('Asia/Ho_Chi_Minh')
    now = datetime.now(vietnam_tz)
    date_str = now.strftime("%d/%m/%Y")

    print(f"📡 Prepare to send {len(deals)} deal onto Discord...")

    # 3. KỸ THUẬT CHIA NHÓM: Cứ 10 deal gửi 1 tin nhắn (Giới hạn của Discord)
    # range(start, stop, step) -> nhảy bước 10
    for i in range(0, len(deals), 10):
        chunk = deals[i:i + 10]
        embeds = []
        
        for deal in chunk:
            # Tạo khung hiển thị (Embed) cho từng game
            embed = {
                "title": deal['title'],
                "url": f"https://store.steampowered.com/app/{deal['steamAppID']}",
                "color": 15158332, # Màu đỏ rực rỡ
                "fields": [
                    {"name": "Original Price", "value": f"${deal['normalPrice']}", "inline": True},
                    {"name": "Saled Price", "value": f"${deal['salePrice']}", "inline": True},
                    {"name": "Saving", "value": f"📉 {deal['savings']}%", "inline": True}
                ],
                "image": {"url": f"https://cdn.cloudflare.steamstatic.com/steam/apps/{deal['steamAppID']}/header.jpg"},
                "footer": {"text": "Data from Steam API"}
            }
            embeds.append(embed)

        # 4. Gom nhóm vào Payload
        # Nếu là nhóm đầu tiên (i=0) thì hiện tiêu đề to, các nhóm sau hiện tiêu đề phụ
        part_number = (i // 10) + 1
        total_parts = (len(deals) + 9) // 10
        
        content_msg = f"📢 **NEWS STEAM DEAL - DATE {date_str} (Part {part_number}/{total_parts})** 📢\nCome get some today deals!" if i == 0 else f"--- NExt (Part {part_number}/{total_parts}) ---"

        payload = {
            "content": content_msg,
            "embeds": embeds
        }
        
        # 5. Thực hiện gửi request
        response = requests.post(webhook_url, json=payload)
        
        if response.status_code == 204:
            print(f"✅ Sent complete part {part_number}")
        else:
            print(f"❌ ERR Part {part_number}: {response.status_code} - {response.text}")
