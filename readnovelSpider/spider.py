import json
from pprint import pprint
from urllib.parse import urljoin

import requests
from pyquery import PyQuery as pq


def get_html(url, headers):
    '''
        url: download url
        headers: request header info
    '''
    try:
        req = requests.get(url=url, headers=headers, timeout=10)
        if req.status_code == 200:
            return req.text
    except requests.exceptions.RequestException as e:
        print('[*] request exception ', e)


def save_to_json_file(data):
    '''
       data: save page data
    '''
    with open('story.json', 'a') as fs:
        fs.write(json.dumps(data, ensure_ascii=False))


def parse_page(response):
    '''
       resposne: parse content
    '''
    doc = pq(response)

    books_list = doc('.right-book-list ul')

    books = {}

    books_list = []

    for item in books_list.find('li').items():
        book_image = item.find('.book-img a img').attr('src')
        books['book_image'] = urljoin('https://www.readnovel.com', book_image)
        links = item.find('.book-info h3 a').attr('href')
        books['title'] = item.find('.book-info h3 a').text()
        books['author'] = item.find('.default').text()
        books['story_type'] = item.find('.org').text()
        books['status'] = item.find('.red').text()
        books['numbers'] = item.find('.blue').text()
        books['desc'] = item.find('.intro').text()
        books['links'] = urljoin('https://www.readnovel.com', links)

        books_list.append(books)

        #pprint(books)

    save_to_json_file(books_list)


def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }

    for page_number in range(1, 100+1):
        url = 'https://www.readnovel.com/finish?pageSize=10&gender=2&catId=-1&isFinish=1&isVip=-1&size=-1&updT=-1&orderBy=0&pageNum={0}'.format(page_number)
        response = get_html(url, headers)

        parse_page(response)

if __name__ == '__main__':
    main()



