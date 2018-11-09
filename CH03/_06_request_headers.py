from urllib import request, parse

url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Host': 'httpbin.org'
}

dict = {
    'test': 'Germey'
}
data = bytes(parse.urlencode(dict), encoding='utf-8')
# req = request.Request(url=url, data=data, headers=headers, method='POST')
req = request.Request(url=url, data=data, method='POST')
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)')
response = request.urlopen(req)
print(response.read().decode('utf-8'))