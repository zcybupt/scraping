import requests

url = 'http://137.1.1.128:8050/render.json?url=https://httpbin.org'
response = requests.get(url)
print(response.text)