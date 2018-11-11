from urllib.parse import quote

# 将内容转化为 URL 编码格式. URL 中带有中文参数时, 可用这个方法将中文转化为 URL 编码
keyword = '壁纸'
url = 'https://www.baidu.com/s?wd=' + quote(keyword)
print(url)