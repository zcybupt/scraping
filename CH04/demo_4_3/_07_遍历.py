from pyquery import PyQuery as pq

html = ''
with open('./_03.html') as file:
    for line in file:
        html += line

doc = pq(html)
# li = doc('.item-0.active')
# print(li)
# print(str(li))

lis = doc('li').items()
print(type(lis))
for li in lis:
    print(li, type(li))
