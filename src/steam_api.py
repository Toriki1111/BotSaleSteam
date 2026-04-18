import requests

def get_top_deals():
    #data from  CheapShark API
    url = "https://www.cheapshark.com/api/1.0/deals?storeID=1&upperPrice=50"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return []
