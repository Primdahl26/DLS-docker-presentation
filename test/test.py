import requests

req = requests.get('https://api.github.com')

print(req)

print(req.json())
