from urllib.request import urlopen

response = urlopen('https://www.baidu.com')
print(response.read().decode('utf-8'))
