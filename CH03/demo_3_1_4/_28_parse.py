from urllib.robotparser import RobotFileParser
from urllib.request import urlopen

rp = RobotFileParser()
rp.parse(urlopen('https://cuiqingcai.com//robots.txt').read().decode('utf-8').split('\n'))
print(rp.can_fetch('*', 'https://cuiqingcai.com/1052.html'))