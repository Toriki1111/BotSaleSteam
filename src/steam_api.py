import requests

def get_top_deals(): # Phải đặt tên chính xác là get_top_deals
    # Code lấy dữ liệu từ CheapShark API của Phú
    url = "https://www.cheapshark.com/api/1.0/deals?storeID=1&upperPrice=50"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return []