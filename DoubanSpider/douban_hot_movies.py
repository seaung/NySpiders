#!/usr/bin/env python3
import json
from pprint import pprint
import requests


def download(url, headers):
    try:
        response = requests.get(url=url, headers=headers, timeout=10)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException as e:
        print('[(*)] request exception %s ' % (e, ))
        return None


def save_to_file(data):
    with open('hot_movie.json', 'a') as fs:
        fs.write(json.dumps(data, ensure_ascii=False))


def parse_movie_item(source):
    hot_movies = {}
    hot_list = []
    datas = json.loads(source)
    # pprint(data)
    for item in datas['data']:
        directors = item['directors']
        rate = item['rate']
        cover_x = item['cover_x']
        star = item['star']
        title = item['title']
        url = item['url']
        casts = item['casts']
        cover = item['cover']
        movie_id = item['id']
        cover_y = item['cover_y']

        hot_movies = {
                "directors": directors,
                "rate": rate,
                "cover_x": cover_x,
                "star": star,
                "url": url,
                "casts": casts,
                "title": title,
                "movie_id": movie_id,
                "cover_y": cover_y
            }
        hot_list.append(hot_movies)
    save_to_file(hot_list)
    pprint(hot_list)



if __name__ == '__main__':
    print('start')
    movie_index_list = [0, 20, 40, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360]

    headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
        }
    for index in movie_index_list:
        url = 'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start={0}'.format(index)
        source = download(url, headers)
        parse_movie_item(source)

       
