import re

content = 'asa64sd8f583a4sg47s8fd67sd4n3gs5fh7ey'
# re.sub() 第一个参数匹配所有的数字, 第二个参数为替换成的字符串, 第三个参数为原字符串
content = re.sub('\d+', '', content)
print(content)