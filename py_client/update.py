import requests

headers = {'Authorization': 'Bearer fe50a0254c0876e5bb55d241213fa45960bcdce1'}
# endpoint = "http://localhost:8000/api/products/4/" 
endpoint = "http://localhost:8000/api/v2/products-abc/4/update/" 

data = {
    "title": "I hope v2 is working properly",
    "content": "Never give up",
    "price": 250
}

get_response = requests.put(endpoint, json=data, headers=headers) 
print(get_response.json())