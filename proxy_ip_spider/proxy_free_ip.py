#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import logging
import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


try:
    reload(sys)
    sys.setdefaultencoding = "utf-8"
except NameError:
    try:
        from importlib import reload
        reload(sys)
        sys.setdefaultencoding = "utf-8"
    except ImportError:
        from imp import reload
        reload(sys)
        setdefaultencoding = "utf-8"


def downloader(url, headers):
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException as e:
        logger.info("[!] request exceptions {0}".format(e))
        return None


def parse_proxy_list(html):
    try:
        soup = BeautifulSoup(html, "lxml")

        count = 0

        proxy_ip_list = []

        proxy_list = soup.find("table", attrs={"class": "list"})

        while count < 5:
            for item in proxy_list.find_all('tr')[1:]:
                ip = item.find_all('td')[0].get_text()
                port = item.find_all('td')[1].get_text()
                proxy_ip_list.append(':'.join([ip, port]))

            count = count + 1

            if count == 5:
                break
        logger.info("[*] proxy ip list : {0}".format(proxy_ip_list))
    except Exception as e:
        logger.info("[!] exceptions {0}".format(e))


def main():
    try:
        url = "http://www.mimiip.com/"
        headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
        html = downloader(url, headers)
        parse_proxy_list(html)
    except Exception as e:
        logger.info("[!] exception ~_~ {0}".format(e))
        return None


if __name__ == '__main__':
    main()

