from urllib.request import urlopen

response = urlopen('https://www.python.org')
print('status = ', response.status)
print('headers: ', response.getheaders())
print('server header: ', response.getheader('Server'))