from pyquery import PyQuery as pq

html = ''
with open('./_03.html') as file:
    for line in file:
        html += line

doc = pq(html)
li = doc('.item-0.active')
print(li)
li.remove_class('active')
print(li)
li.add_class('active')
print(li)
