from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException

browser = webdriver.Chrome()
try:
    browser.get('https://www.googled.com')
except TimeoutException:
    print('Time Out')

try:
    browser.find_element_by_id('test')
except NoSuchElementException:
    print('No Such Element')
finally:
    browser.close()