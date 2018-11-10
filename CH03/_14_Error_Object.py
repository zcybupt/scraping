import socket
import urllib.error
import urllib.request

try:
    response = urllib.request.urlopen('https://cuiqingcai.com/index.htm', timeout=0.01)
except urllib.error.URLError as e:
    print(type(e.reason))
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')