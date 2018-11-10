from urllib.parse import parse_qs

# 反序列化, 将请求参数转换为字典
query = 'name=germy&age=22'
print(parse_qs(query))