from urllib.robotparser import RobotFileParser
from urllib.request import urlopen

rp = RobotFileParser()
rp.parse(urlopen('https://www.jianshu.com/robots.txt').read().decode('utf-8').split('\n'))
print(rp.can_fetch('*', 'https://www.jianshu.com/p/b67554025d7d'))
print(rp.can_fetch('*', 'https://www.jianshu.com/search?q=python&page=1&type=collections'))