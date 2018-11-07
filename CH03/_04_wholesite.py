from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen('http://en.wikipedia.org' + pageUrl)
    bsObj = BeautifulSoup(html, features='html.parser')
    try:
        print(bsObj.h1.get_text())
        print(bsObj.find(id='mw-content-text').findAll('p')[0])
        print(bsObj.find(id='ca-edit').find('span').span('a').attrs['href'])
    except AttributeError:
        print('页面属性缺少')

    for link in bsObj.findAll('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print('>>>>>>>>>>>>> ' + newPage + ' <<<<<<<<<<<<<\n')
                pages.add(newPage)
                getLinks(newPage)

getLinks('')