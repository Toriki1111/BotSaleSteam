import requests
import os
from dotenv import load_dotenv
from datetime import datetime
import pytz

load_dotenv()

def send_to_discord(deals):
    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
    
    # Lấy ngày hiện tại theo múi giờ Việt Nam (ICT)
    vietnam_tz = pytz.timezone('Asia/Ho_Chi_Minh')
    now = datetime.now(vietnam_tz)
    date_str = now.strftime("%d/%m/%Y") # Định dạng: Ngày/Tháng/Năm

    payload = {
        "content": f"📢 **DANH SÁCH DEAL HỜI STEAM - NGÀY {date_str}**\n@everyone Phú ơi, vào check kèo thơm hôm nay nè!",
        "embeds": []
    }

def send_to_discord(deals):
    # Thêm dòng này để ưu tiên lấy từ GitHub Secrets, nếu không có thì lấy từ .env local
    webhook_url = os.getenv("DISCORD_WEBHOOK") or os.getenv("DISCORD_WEBHOOK_URL")
    
    if not webhook_url:
        print("Lỗi: Không tìm thấy Webhook URL trong cả .env và GitHub Secrets!")
        return
    
    if not deals:
        return
    
    # Tạo một thông báo đẹp mắt (Embed)
    embeds = []
    for deal in deals[:10]: # Lấy tối đa 10 deal hot nhất
        embed = {
            "title": deal['title'],
            "url": f"https://store.steampowered.com/app/{deal['steamAppID']}",
            "color": 15158332, # Màu đỏ rực cho deal 90%
            "fields": [
                {"name": "Giá gốc", "value": f"${deal['normalPrice']}", "inline": True},
                {"name": "Giá giảm", "value": f"${deal['salePrice']}", "inline": True},
                {"name": "Mức giảm", "value": f"📉 {deal['savings']}%", "inline": True}
            ],
            "image": {"url": f"https://cdn.cloudflare.steamstatic.com/steam/apps/{deal['steamAppID']}/header.jpg"}
        }
        embeds.append(embed)

    payload = {
        "content": "🔥 **CẢNH BÁO DEAL STEAM > 90% HÔM NAY** 🔥",
        "embeds": embeds
    }
    
    requests.post(webhook_url, json=payload)