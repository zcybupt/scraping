from pyquery import PyQuery as pq

html = ''
with open('./_03.html') as file:
    lineList = file.readlines()
    for line in lineList:
        html += line

doc = pq(html)
li = doc('.list .item-0.active')
print(li.siblings('.active'))
