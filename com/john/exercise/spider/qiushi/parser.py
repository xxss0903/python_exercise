
# coding:utf8
import re


class ParseHtml:
    def parse(self, html):
        content = html.decode('utf-8')
        pattern = re.compile('<div class="content">.*?</div>', re.S)
        items = re.findall(pattern, content)
        return items
