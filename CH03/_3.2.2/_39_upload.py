import requests

files = {'file': open('../_3.2.1/favicon.ico', 'rb')}
r = requests.post('http://httpbin.org/post', files=files)
print(r.text)