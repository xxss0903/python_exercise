# coding=utf-8
import re
import urllib


class Parser(object):

    def __init__(self, html):
        self.html = html
        pass

    def getImg(self):
        pattern = r'src="(.+?\.jpg)" pic_ext'
        imgre = re.compile(pattern)
        imgList = re.findall(imgre, self.html)

        x = 0
        for imgurl in imgList:
            # 将远程数据下载到本地,使用urlretrieve
            print imgurl
            urllib.urlretrieve(imgurl, '%s.jpg' % x)
            x+=1


        pass