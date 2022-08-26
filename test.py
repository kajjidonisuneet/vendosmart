import requests

# BASE_URL = 'http://127.0.0.1:5000/vendor_data'

# response = requests.post(BASE_URL, json={'name':'suneet', 'location':'banglore', 'rating':4})

BASE_URL = 'http://127.0.0.1:5000/vendor_search'

response = requests.get(BASE_URL+'?name=suneet&rating=10')

print(response.json())