from steam_api import fetch_90_percent_deals
from notifier import send_to_discord

def main():
    print("Đang quét deal hời...")
    deals = fetch_90_percent_deals()
    if deals:
        send_to_discord(deals)
        print(f"Đã gửi {len(deals)} deal lên Discord!")
    else:
        print("Hôm nay không có deal nào giảm trên 90% rồi.")

if __name__ == "__main__":
    main()