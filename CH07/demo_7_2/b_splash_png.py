import requests

url = 'http://137.100.100.128:8050/render.png?url=https://www.jd.com&wait=3&width=1000&height=700'
response = requests.get(url)
with open('jd.png', 'wb') as file:
    file.write(response.content)
