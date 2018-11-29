from urllib.parse import urlparse

"""
scheme 参数只有在 URL 中不包含 scheme 信息时才生效.
如果 URL 中有 scheme 信息, 就会返回解析出的scheme
"""
result = urlparse('www.baidu.com/index.html;user?id=5#comment', scheme='https')
print(result)