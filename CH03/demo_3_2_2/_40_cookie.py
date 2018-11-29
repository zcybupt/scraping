import requests

r = requests.get('https://www.baidu.com')
print(r.cookies)
for key, value in r.cookies.items():  # items() 方法将 RequestCookieJar 转化为元组组成的列表
    print(key + ' = ' + value)
