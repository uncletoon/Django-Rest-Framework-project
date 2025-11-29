import requests


headers = {'Authorization': 'Token fe50a0254c0876e5bb55d241213fa45960bcdce1'}
endpoint = "http://localhost:8000/api/products/" 

data = {
    "title": "Google Glasses",
    "content": "Now I see what is in your head",
    "price": 500.99
}
get_response = requests.post(endpoint, json=data, headers=headers) 
print(get_response.json())