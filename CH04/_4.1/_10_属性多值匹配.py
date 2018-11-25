from lxml import etree

text = '''
<li class="li li-first"><a href="link.html">first item</a></li>
'''
html = etree.HTML(text)
# contians() 方法第一个参数传入属性名称, 第二个参数传入属性值, 只要此属性包含所传入的属性值就可完成匹配
result = html.xpath('//li[contains(@class, "li")]/a/text()')
print(result)
