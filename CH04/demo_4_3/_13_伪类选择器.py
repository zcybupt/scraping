from pyquery import PyQuery as pq

html = ''
with open('./_03.html') as file:
    for line in file:
        html += line

doc = pq(html)
li = doc('li:first-child')
print(li)
li = doc('li:last-child')
print(li)
li = doc('li:nth-child(2)')
print(li)
li = doc('li:gt(2)')                # 第三个 li 之后的 li 节点
print(li)
li = doc('li:nth-child(2n)')        # 偶数位置的 li 节点
print(li)
li = doc('li:contains(second)')     # 包含 second 文本的节点
print(li)
