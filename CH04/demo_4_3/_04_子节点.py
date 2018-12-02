from pyquery import PyQuery as pq

html = ''
with open('./_03.html') as file:
    inputList = file.readlines()
    for line in inputList:
        html += line

doc = pq(html)
items = doc('.list')
print(type(items))
print(items)
# lis = items.find('li')
# print(type(lis))
# print(lis)
lis = items.children('.active')
print(type(lis))
print(lis)
