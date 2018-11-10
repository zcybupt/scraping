from urllib.parse import urljoin

"""
base_url 提供了三项内容 scheme, netloc, path. 如果这三项在新的链接里不存在就予以补充;
如果新的连接存在, 就用新的连接部分. 而 base_url 中的 params, query 和 fragment 不起作用.
"""
print(urljoin('http://www.baidu.com', 'FAQ.html'))
print(urljoin('http://www.baidu.com', 'https://cuiqingcai.com/FAQ.html'))
print(urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html'))
print(urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html?question=2'))
print(urljoin('http://www.baidu.com?wd=abc', 'https://cuiqingcai.com/index.php'))
print(urljoin('http://www.baidu.com', '?category=2#comment'))
print(urljoin('http://www.baidu.com#comment', '?category=2'))