from pyquery import PyQuery as pq

html = ''
with open('./_03.html') as file:
    for line in file:
        html += line

doc = pq(html)
a = doc('.item-0.active a')
print(a)
print(a.text())
print("==================================================================")

li = doc('.item-0.active')
print(li)
print(li.html())
print("==================================================================")

li = doc('li')
print(li.html())
print(li.text())
print(type(li.text()))
