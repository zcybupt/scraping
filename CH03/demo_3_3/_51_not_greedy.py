import re

# 将 .* 变为 .*? 转变为非贪婪模式, 将会匹配尽可能少的字符
content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^He.*?(\d+).*Demo$', content)
print(result)
print(result.group(1))
