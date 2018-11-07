from CH03._05_random_link import *

allExtLinks = set()
allIntLinks = set()

def getAllExternalLinks(siteUrl):
    html = urlopen(siteUrl)
    bsObj = BeautifulSoup(html, features="html.parser")
    internalLinks = getInternalLinks(bsObj, splitAddress(siteUrl)[0])
    externalLinks = getExternalLinks(bsObj, splitAddress(siteUrl)[0])
    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
    print(link)
    for link in internalLinks:
        if link not in allIntLinks:
            print("即将获取链接的URL是：" + link)
    allIntLinks.add(link)
    getAllExternalLinks(link)
    getAllExternalLinks("http://oreilly.com")
