import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/70.0.3538.77 Safari/537.36'
}
r = requests.get('http://www.jianshu.com', headers=headers)
print(r.status_code)
exit() if not r.status_code == requests.codes.ok else print('Request Successfully')