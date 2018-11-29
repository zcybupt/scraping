from urllib.robotparser import RobotFileParser

rp = RobotFileParser()
rp.set_url('https://cuiqingcai.com/robots.txt')
rp.read()
print(rp.can_fetch('*', 'https://cuiqingcai.com/1052.html'))
print(rp.can_fetch('*', 'https://cuiqingcai.com/?s=%E7%88%AC%E8%99%AB'))