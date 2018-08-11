import json
import requests
from requests.exceptions import RequestException
from lxml import etree


def download(url, headers):
    try:
        response = requests.get(url=url, headers=headers, timeout=10)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException as e:
        print('[(*)] requests exceptions %s ' %(e, ))
        return None


def save_to_json_format_file(file_data):
    with open('movies.json', 'a') as fs:
        fs.write(json.dumps(file_data, ensure_ascii=False))


def xparse(source):
    movies = []
    movies_dict = {}

    response = etree.HTML(source)

    ul = response.xpath('//div[@class="mod-bd"]/ul[@class="lists"]')[0]
    lis = ul.xpath('./li')
    
    for node in lis:
        movie_id = node.xpath('@id')[0]
        title = node.xpath('@data-title')[0]
        score = node.xpath('@data-score')[0]
        star = node.xpath('@data-star')[0]
        release = node.xpath('@data-release')[0]
        duration = node.xpath('@data-duration')[0]
        actors = node.xpath('@data-actors')[0]
        thumbnail = node.xpath('.//img/@src')[0]
        poster_url = node.xpath('.//li[@class="poster"]/a[@class="ticket-btn"]/@href')[0]
        category = node.xpath('@data-category')[0]
        movies_dict = {
                "title": title,
                "score": score,
                "star": star,
                "release": release,
                "duration": duration,
                "actors": actors,
                "id": movie_id,
                "category": category,
                "thumbnail": thumbnail,
                "poster_url": poster_url
            }
        movies.append(movies_dict)

    save_to_json_format_file(movies)
        


if __name__ == '__main__':
    url = 'https://movie.douban.com/cinema/nowplaying/shenzhen/'
    headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
        }
    source = download(url, headers)
    xparse(source)
