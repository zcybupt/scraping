import re

content = 'Extra strings Hello 1234567 World_This is a Regex Demo Extra strings'
# match() 方法从字符串的开头开始匹配, 一旦开头不匹配将匹配失败
# result = re.match('Hello.*?(\d+).*?Demo', content)

# search() 在匹配时会扫描整个字符串, 然后返回第一个成功匹配的结果
result = re.search('Hello.*?(\d+).*?Demo', content)
print(result)
