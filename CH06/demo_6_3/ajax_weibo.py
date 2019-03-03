from urllib.parse import urlencode
import requests
from pyquery import PyQuery as pq
from pymongo import MongoClient

base_url = 'https://m.weibo.cn/api/container/getIndex?display=0&retcode=6102&'

headers = {
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/2830678474',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/72.0.3626.119 Mobile Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}


def get_page(page):
    params = {
        'type': 'uid',
        'value': '2830678474',
        'containerid': '1076032830678474',
        'page': page
    }

    if (page == 1):
        params.pop('page')

    url = base_url + urlencode(params)
    print(url)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('Error', e.args)


def parse_page(json):
    if json:
        items = json.get('data').get('cards')
        for item in items:
            item = item.get('mblog')
            weibo = {}
            try:
                weibo['id'] = item.get('id')
                weibo['text'] = pq(item.get('text')).text()
                weibo['attitudes'] = item.get('attitudes_count')
                weibo['comments'] = item.get('comments_count')
                weibo['reposts'] = item.get('reposts_count')
            except:
                continue
            yield weibo


if __name__ == '__main__':
    client = MongoClient('mongodb://10.128.240.90:27017')
    db = client['weibo']
    collection = db['weibo']

    for page in range(1, 11):
        json = get_page(page)
        results = parse_page(json)
        for result in results:
            print(result)
            if collection.insert(result):
                print('Saved to MongoDB')
