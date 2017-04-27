from com.john.exercise.spider.taobaomm2.spider_parser import Parser
from com.john.exercise.spider.taobaomm2.spider_reader import Reader


baseUrl = 'http://mm.taobao.com/json/request_top_list.htm'
reader = Reader(baseUrl)
html = reader.read()
parser = Parser(html)
parser.downloadImg()
