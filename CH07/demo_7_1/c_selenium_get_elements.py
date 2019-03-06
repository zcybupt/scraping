from selenium import webdriver

broswer = webdriver.Chrome()
broswer.get('https://www.taobao.com')
lis = broswer.find_elements_by_css_selector('.service-bd li')
for li in lis:
    print(li.text)
broswer.close()