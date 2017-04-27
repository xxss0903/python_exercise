#-*- coding: utf-8 -*-


import jiemoren as sp

# 腾讯动漫爬虫

if __name__ == '__main__':

    site = 'http://ac.qq.com/ComicView/index/id/530955/cid/1' #漫画的起始页面

    #定义一个爬虫
    spider = sp.Spider(site, begin=0, end=-1, save_folder='E:\Temp\cartoon\jiemoren\\')
    spider.open_browser()

    pass
