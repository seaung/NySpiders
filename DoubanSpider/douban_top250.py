import time

import requests
from bs4 import BeautifulSoup


def download(url, headers, retries_numbers=6):
    try:
        resp = requests.get(url=url, headers=headers, timeout=10)
        if resp.statuc_code == 200:
            return resp.text
    except requests.exceptions.RequestException as e:
        if retries_numbers > 0:
            time.sleep(10)
            return download(url, headers, retries_numbers=-1)


def parser_movie_top_250(response):
    soup = BeautifulSoup(response, 'lxml')

    movie_top_250_list = []
    movie_top_250_dict = {}

    movie_list = soup.find('ol', {'class': 'grid_view'})

    if movie_list:
        movie_details = movie_list.find_all('li')

        for movie in movie_details:
            index = movie.find('em').string
            movie_url = movie.find('a')
            movie_url = movie_url['href']
            img = movie.find('img')
            img = img['src']
            title = movie.find('span', {'class': 'title'}).get_text()
            content = movie.find('div', {'class': 'bd'}).p.get_text()
            star = movie.find('span', {'class': 'rating_num'}).get_text()
            quote = movie.find('span', {'class': 'quote'}).span.get_text()

            movie_top_250_dict['index'] = index
            movie_top_250_dict['movie_url'] = movie_url
            movie_top_250_dict['img'] = img
            movie_top_250_dict['title'] = title
            movie_top_250_dict['content'] = content
            movie_top_250_dict['star'] = star
            movie_top_250_dict['quote'] = quote

            movie_top_250_list.append(movie_top_250_dict)


def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }

    for page_number in range(0, 250, 25):
        url = 'https://movie.douban.com/top250?start={0}&filter='.format(page_number)

        response = download(url, headers)

        parser_movie_top_250(response)


if __name__ == '__main__':
    main()


