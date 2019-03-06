from selenium import webdriver
from selenium.webdriver.common.by import By

broswer = webdriver.Chrome()
broswer.get('https://www.taobao.com')
input_1 = broswer.find_element_by_id('q')
input_2 = broswer.find_element_by_css_selector('#q')
input_3 = broswer.find_element_by_xpath('//*[@id="q"]')
print(input_1, input_2, input_3, sep='\n')

input_4 = broswer.find_element(By.ID, 'q')
print(input_4)
broswer.close()
