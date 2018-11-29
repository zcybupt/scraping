import requests

files = {'file': open('../demo_3_2_1/favicon.ico', 'rb')}
r = requests.post('http://httpbin.org/post', files=files)
print(r.text)