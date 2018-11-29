from urllib.parse import urlencode

params = {
    'name': 'germy',
    'age': 22
}
base_url = 'http://www.baidu.com?'
url = base_url + urlencode(params)  # urlencode() 方法将其序列化为 GET 请求参数
print(url)