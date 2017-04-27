# coding=utf-8
import re


class Parser:

    def __init__(self, html):
        self.html = html

    def parse(self):
        # 解析html
        reg = '<div class="list-item".*?pic-word.*?<a href="(.*?)".*?<img src="(.*?)".*?<a class="lady-name.*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>'
        pattern = re.compile(reg, re.S)
        items = re.findall(pattern, self.html)
        for item in items:
            print item[0], item[1]
        pass


    def downloadImg(self):
        # 下载图片
        self.parse()

        pass