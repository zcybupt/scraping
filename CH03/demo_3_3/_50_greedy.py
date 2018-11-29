import re

"""
    在贪婪匹配下 .* 会匹配尽可能多的字符. 正则表达式中 .* 后边是 \d+, 也就是最少一个数字,
    并没有指定具体多少个数字, 因此 .* 就尽可能匹配多的字符, 就把 123456 匹配了, 给 \d+ 留
    下一个 7, 最后得到的匹配内容就只有一个 7
"""
content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^He.*(\d+).*Demo$', content)
print(result)
print(result.group())
print(result.group(1))

