# coding=utf-8
from com.john.exercise.spider.taobaomm.downloader import Downloader
from com.john.exercise.spider.taobaomm.parser import Parser

baseUrl = 'https://tieba.baidu.com/p/2460150866'

downloader = Downloader(baseUrl)
html = downloader.getHtml()
print html

parser = Parser(html)
parser.getImg()