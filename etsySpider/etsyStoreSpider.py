from core.urls import Urls
from core.downloader import Downloader
from core.xparse import Xparse
from core.utils import save_to_json


class Spider(object):
    def __init__(self):
        self.urls = Urls()
        self.download = Downloader()
        self.parse = Xparse()
        self.headers = {}

    def crawl(self, root_url):
        pass


if __name__ == "__main__":
    url = ""
    spider = Spider()
    spider.crawl()
