import requests.cookies

cookies = '_xsrf=uUq8YhWMu4E3n5uBbanTrkAzsMzSjXIJ; _zap=8c258511-1e22-4d30-bea9-61ea106290db; d_c0="AJDow_Y2aA6PTnwAnL8yeeI7j8LvgWLyyt0=|1540291898"; tst=r; q_c1=12eb8ca00f98451898542474ce016dd6|1540947576000|1540947576000; l_cap_id="NmEzYTg4MzI3ZTZiNDE4ZThjNWRhYjJmZDQyODc1ZjQ=|1541939430|2412ce97a185b02df795a5b26d7a1678300290a1"; r_cap_id="Y2E4YzNkMzc4ODcxNGRmM2E3NDk2Nzc2ODNlYzZjN2U=|1541939430|847101ae6e1c4460ad3e67eb891e9d5e6a73d923"; cap_id="NDY1Zjk0MTg5ZmMzNDYwMzk5NTY4Yzg3NDcyZDIwNTQ=|1541939430|680e6fe0ee7efe92f70f02c397fc574af959fdae"; tgw_l7_route=69f52e0ac392bb43ffb22fc18a173ee6; capsion_ticket="2|1:0|10:1542098409|14:capsion_ticket|44:ZmNjMDA1NjJkNjdhNDA5ZWEyZjdlYTE3NzQ5NGRhOWU=|b4ef6a08c5929f72abad1aa4ae2da55b821ca6c89288d5d0027fdc0360ad76da"; z_c0="2|1:0|10:1542098410|4:z_c0|92:Mi4xY3hOVEJBQUFBQUFBa09qRDlqWm9EaVlBQUFCZ0FsVk42dHZYWEFDalh5aUxKaU5mSjZYUG9EdjVQQ0dPcVJhUlp3|9dad60db3a633e214b3ee4d4c52416465a8d339a5ec14f5caf90a19d9e6646bc"'
jar = requests.cookies.RequestsCookieJar()
headers = {
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}
for cookie in cookies.split(';'):
    key, value = cookie.split('=', 1)
    jar.set(key, value)

r = requests.get('http://www.zhihu.com', cookies=jar, headers=headers)
print(r.text)
