#!/usr/bin/env python3
import requests
from requests.exceptions import RequestException
from lxml import etree


def downloader(url, headers):
    try:
        response = requests.get(url=url, headers=headers, timeout=10)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException as e:
        return None


def xparse(source):
    response = etree.HTML(source)

    ul = response.xpath('//ul[@class="item_con_list"]/li')
    for node in ul:
        print(node)



if __name__ == '__main__':
    url = 'https://www.lagou.com/jobs/list_python?px=default&city=%E5%85%A8%E5%9B%BD#filterBox'
    headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52'
        }
    source = downloader(url, headers)
    xparse(source)
