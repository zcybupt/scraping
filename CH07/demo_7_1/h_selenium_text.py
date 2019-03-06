from selenium import webdriver

browser = webdriver.Chrome()
url = 'https://www.zhihu.com/explore'
browser.get(url)
input = browser.find_element_by_id('zu-top-add-question')
print(input.id)
print(input.location)
print(input.tag_name)
print(input.text)
print(input.size)
browser.close()