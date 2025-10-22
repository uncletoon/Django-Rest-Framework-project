import requests

headers = {'Authorization': 'Bearer fe50a0254c0876e5bb55d241213fa45960bcdce1'}
endpoint = "http://localhost:8000/api/products/1/update/" 

data = {
    "title": "Try this updates",
    "price": 153
}

get_response = requests.put(endpoint, json=data, headers=headers) 
print(get_response.json())