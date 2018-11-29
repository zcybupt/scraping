from lxml import etree

text = '''
<div>
<ul>
<li class="item-0"><a href="link1.html"><span>first item</span></a></li>
<li class="item-1"><a href="link2.html"><span>second item</a></li>
<li class="item-inactive"><a href="link3.html"><span>third item</a></li>
<li class="item-1"><a href="link4.html"><span>fourth item</a></li>
<li class="item-0"><a href="link5.html"><span>fifth item</a></li>
</ul>
</div>
'''

html = etree.HTML(text)
result = html.xpath('//li[1]/ancestor::*')                      # 获取所有祖先节点
print(result)
result = html.xpath('//li[1]/ancestor::div')
print(result)
result = html.xpath('//li[1]/attribute::*')                     # 获取所有属性值
print(result)
result = html.xpath('//li[1]/child::a[@href="link1.html"]')     # 获取所有直接子节点
print(result)
result = html.xpath('//li[1]/descendant::span')                 # 获取所有子孙节点
print(result)
result = html.xpath('//li[1]/following::*[2]')                  # 获取当前节点之后的所有节点
print(result)
result = html.xpath('//li[1]/following-sibling::*')             # 获取当前节点之后的所有同级节点
print(result)
