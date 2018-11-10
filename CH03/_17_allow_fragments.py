from urllib.parse import urlparse

result = urlparse('http://www.baidu.com/index.html;user?id=5#comment', allow_fragments=False)

# URL 中不包含 parms 和 query 时, fragment 便会被解析为 path 的一部分
# result = urlparse('www.baidu.com/index.html#comment', allow_fragments=False)

print(result.scheme, result[0], result.netloc, result[1], sep='\n')