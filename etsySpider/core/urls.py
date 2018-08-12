#!/usr/bin/env python3


class Urls(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):
        if url is None:
            return

        if not url in self.new_urls and not url in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        if len(urls) == 0:
            return

        for url in urls:
            self.add_new_url.add(url)

    def has_new_url(self):
        return len(self.add_new_urls) != 0

    def get_url(self):
        url = self.add_new_url.pop()
        self.old_urls.add(url)
        return url

