#!/usr/bin/env python3
import urllib.request
import urllib.parse
import requests
from requests.exceptions import RequestException


class Downloader(object):
    def download(self, url, headers):
        try:
            response = requests.get(url=url, headers=headers, timeout=10)
            if response.status_code == 200:
                return response.text
            return None
        except RequestException as e:
            print('[(*)] requests exception %s ' % (e, ))
            return None

    def tools_download(self, url, headers):
        pass

