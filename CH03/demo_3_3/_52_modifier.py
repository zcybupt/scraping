import re

content = """Hello 1234567 World_This
is a Regex Demo
"""

# . 匹配的是除换行符之外的任意字符, 当遇到换行符时 .*? 就不能匹配
# re.S 修饰符的作用是使 . 匹配包括换行符在内的所有字符
result = re.match('^He.*?(\d+).*?Demo$', content, re.S)
print(result.group(1))

"""
常用修饰符
    re.I            使匹配对大小写不敏感
    re.L            做本地化识别(local-aware)匹配
    re.M            多行匹配, 影响^和$
    re.S            使 . 匹配包括换行符在内的所有字符
    re.U            根据 Unicode 字符集解析字符. 这个标志影响\w, \W, \b 和 \B
    re.X            该标志通过给予更灵活的格式以便使正则表达式更易于理解
"""