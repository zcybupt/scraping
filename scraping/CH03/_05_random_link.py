from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

# 获取页面所有内链列表
def getInternalLinks(bsObj, includeUrl):
    internalLinks = []
    for link in bsObj.findAll('a', href = re.compile('^(/|.*' + includeUrl + ')')):
        if link.attrs['href'] not in internalLinks:
            internalLinks.append(link.attrs['href'])
    return internalLinks

def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    for link in bsObj.findAll('a', href=re.compile('^(http|www)((?!' + excludeUrl + ').)*$')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def splitAddress(address):
    return address.replace('http://', '').split('/')

def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html, features='html.parser')
    externalLinks = getExternalLinks(bsObj, splitAddress(startingPage)[0])
    if len(externalLinks) == 0:
        internalLinks = getInternalLinks(startingPage)
        # return getNextExternalLink(internalLinks[random.randint(0, len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks) - 1)]

def followExternalOnly(startingSite):
    externalLink = getExternalLinks('http://oreilly.com')
    print('随机外链为: ' + externalLink)
    followExternalOnly(externalLink)

followExternalOnly('http://oreilly.com')