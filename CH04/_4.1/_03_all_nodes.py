from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//*')  # * 代表匹配所有节点
result = html.xpath('//li')   # 获取所有 li 节点
print(result)
print(result[0])
