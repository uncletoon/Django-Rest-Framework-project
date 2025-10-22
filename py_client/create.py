import requests


headers = {'Authorization': 'Bearer fe50a0254c0876e5bb55d241213fa45960bcdce1'}
endpoint = "http://localhost:8000/api/products/" 

data = {
    "title": "Tomato",
    "content": "I can't let you eat it ma",
    "price": 500.99
}
get_response = requests.post(endpoint, json=data, headers=headers) 
print(get_response.json())