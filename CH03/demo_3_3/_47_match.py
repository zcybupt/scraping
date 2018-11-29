import re

content = 'Hello 123 4567 World_This is a Regex Demo'
print(len(content))
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
print(type(result))
print(result)
print(len(result.group()))
print(type(result.group()))
print(result.group())   # group() 输出正则表达式规则所匹配的内容
print(result.span())    # span() 输出匹配到的字符串在原字符串中的位置范围