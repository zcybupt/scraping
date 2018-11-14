import re

"""
 .* 匹配任意字符串
 . 匹配任意字符
 * 匹配前面的字符无限次
"""
content = 'Hello 123 4567 World_This is a Regex Demo'
result = re.match('^Hello.*Demo$', content)
print(result)
print(result.group())
print(result.span())
