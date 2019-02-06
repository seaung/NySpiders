import json
import asyncio
from pprint import pprint
from urllib.parse import urljoin

import aiohttp
from pyquery import PyQuery as pq


async def fetch(session, url):
    '''
        :session: aiohttp.ClientSession object instance
        :url: request url
        :return: response content
    '''
    async with session.get(url) as resq:
        return await resq.text()


'''
async def save_to_json(data):
    '''
       :data: extract page data
    '''
    with open('readonvel.json', 'a') as fs:
        fs.write(json.dumps(data, ensure_ascii=False))
'''


async def parse_page(response):
    '''
        extract page data
        :response: response content
        :return:
    '''
    doc = pq(response)

    book_lists = doc('.right-book-list ul')

    books = {}

    for item in book_lists.find('li').items():
        image_links = item.find('.book-img a img').attr('src')
        books['image_links'] = urljoin('https://www.readnovel.com/finish',
                                       image_links)
        links = item.find('.book-img a').attr('href')
        books['links'] = urljoin('https://www.readnovel.com/finish', links)
        books['title'] = item.find('.book-info h3 a').text()
        books['author'] = item.find('.default').text()
        books['story_type'] = item.find('.org').text()
        books['status'] = item.find('.red').text()
        books['numbers'] = item.find('.blue').text()
        books['desc'] = item.find('.intro').text()
        pprint(books)


async def enggier(url):
    '''
       :url: request url
       :return:
    '''
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url)
        await parse_page(html)


urls = [
    'https://www.readnovel.com/finish?pageSize=10&gender=2&catId=-1&isFinish=1&isVip=-1&size=-1&updT=-1&orderBy=0&pageNum=%d'%page
    for page in range(1, 101)
]


loop = asyncio.get_event_loop()
tasks = [asyncio.ensure_future(enggier(url)) for url in urls]
tasks = asyncio.gather(*tasks)
loop.run_until_complete(tasks)

