import requests

url = 'http://137.100.100.128:8050/render.html?url=https://www.taobao.com&wait=5'
response = requests.get(url)
print(response.text)