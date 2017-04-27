# coding:utf8
from com.john.exercise.spider.qiushi.outputer import Outputer
from com.john.exercise.spider.qiushi.parser import ParseHtml
from com.john.exercise.spider.qiushi.downloader import Downloader


class Spider:
    d = Downloader()
    html = d.readUrl()
    parser = ParseHtml()
    items = parser.parse(html)
    outer = Outputer()
    outer.write(items)
    for item in items:
        print item
    pass












