import requests

# BASE_URL = 'http://127.0.0.1:5000/vendor_data'
# response = requests.delete(BASE_URL+'/1',json={'name':'kajjidonisasduneet'})

# BASE_URL = 'http://127.0.0.1:5000/vendor_data'
# response = requests.put(BASE_URL+'/1',json={'name':'kajjidonisasduneet'})

# BASE_URL = 'http://127.0.0.1:5000/vendor_data'
# response = requests.get(BASE_URL+'/1')

# BASE_URL = 'http://127.0.0.1:5000/vendor_data'
# response = requests.post(BASE_URL, json={'name':'kajjidonisasduneet', 'location':'dharward', 'rating':4, 'skills':'coding'})

BASE_URL = 'http://127.0.0.1:5000/vendor_search'
response = requests.get(BASE_URL+'?name=kajjidoni&rating=1')

print(response.json())