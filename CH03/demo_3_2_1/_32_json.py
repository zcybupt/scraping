import requests

r = requests.get('http://httpbin.org/get')
print(type(r.text))
print(r.json()) # 将返回结果由 JSON 转换为字典
print(type(r.json()))