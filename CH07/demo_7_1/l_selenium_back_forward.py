import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
browser.get('https://www.taobao.com')
browser.get('https://www.bupt.edu.cn')

browser.back()
time.sleep(1)
browser.forward()
