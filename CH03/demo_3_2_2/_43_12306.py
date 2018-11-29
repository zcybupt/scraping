import requests

headers = {
    'Host': '12306.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}
response = requests.get('https://12306.cn', headers=headers, verify=False)
print(response.status_code)