import requests

url = 'https://denkar.pythonanywhere.com/api/login/'
data = {
    'username': 'Den',
    'password': '12345'
}

response = requests.post(url, data=data)

print('Status Code:', response.status_code)
print('Response JSON:', response.json())
