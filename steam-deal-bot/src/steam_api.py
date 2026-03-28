import requests

def fetch_90_percent_deals():
    # storeID=1 là Steam, savings=90 lọc các game giảm từ 90%
    url = "https://www.cheapshark.com/api/1.0/deals?storeID=1&onSale=1"
    response = requests.get(url)
    all_deals = response.json()
    
    # Lọc lại chính xác những game giảm >= 90%
    super_deals = [d for d in all_deals if float(d['savings']) >= 90]
    return super_deals