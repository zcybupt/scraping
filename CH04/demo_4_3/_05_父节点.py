from pyquery import PyQuery as pq

html = ''
with open('./_03.html') as file:
    lineList = file.readlines()
    for line in lineList:
        html += line

doc = pq(html)
items = doc('.list')
# container = items.parent()
# print(type(container))
# print(container)

parents = items.parents('.wrap')
print(type(parents))
print(parents)
