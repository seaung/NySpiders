import json
from lxml import etree


class Xparse(object):
    def __init__(self):
        pass

    def xparse(self, source):
        if source is None:
            return

        response = etree.HTML(source)

        data, urls = self._lxml_parse(response), self._get_new_urls(response)

        return data, urls

    def _get_new_urls(self, response):
        pass

    def _lxml_parse(self, source):
        pass

    def _bs_parse(self, source):
        pass

