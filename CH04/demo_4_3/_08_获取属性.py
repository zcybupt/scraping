from pyquery import PyQuery as pq

html = ''
with open('./_03.html') as file:
    for line in file:
        html += line

doc = pq(html)
# a = doc('.item-0.active a')
# print(a, type(a))
# print(a.attr('href'))
# print(a.attr.href)

a = doc('a')
print(a)
for item in a.items():
    print(item.attr.href)
