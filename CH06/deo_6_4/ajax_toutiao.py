import requests
from urllib.parse import urlencode
import os
from hashlib import md5
from multiprocessing.pool import Pool
import re


def get_page(offset):
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': '微软',
        'autoload': 'true',
        'count': 20,
        'cur_tab': '1'
    }

    url = 'https://www.toutiao.com/api/search/content/?' + urlencode(params)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None


def get_images(json):
    if json.get('data'):
        for item in json.get('data'):
            title = item.get('title')
            images = item.get('image_list')
            if images:
                for image in images:
                    yield {
                        'image': image.get('url'),
                        'title': title
                    }


def save_image(item):
    pattern = r"[\/\\\:\*\?\"\<\>\|\ ]"  # '/ \ : * ? " < > |'
    title = re.sub(pattern, '_', item.get('title'))
    print('title =======> ' + title)
    if not os.path.exists('data/' + title):
        os.mkdir('data/' + title)
    try:
        response = requests.get(item.get('image'))
        if response.status_code == 200:
            file_path = 'data/{0}/{1}.{2}'.format(title, md5(response.content).hexdigest(), 'jpg')
            print('path =======> ' + file_path)
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
            else:
                print('Already Downloaded', file_path)
    except requests.ConnectionError:
        print('Failed to Save Image')


def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        print(item)
        save_image(item)


GROUP_START = 1
GROUP_END = 20

if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main, groups)
    pool.close()
    pool.join()