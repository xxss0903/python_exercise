#-*- coding: utf-8 -*-

import cartoon_cat as cc

if __name__ == '__main__':

    site = 'http://www.tazhe.com/mh/9068/'

    crawler = cc.CartoonCat(
        site=site,                                  # 漫画首页
        begin=52,                                    # 起始章节
        end=-1,                                     # 结束章节
        save_folder='E:\Temp\cartoon',            # 保存路径，不存在会自动创建
        browser=cc.BrowserType.PHANTOMJS,           # 浏览器类型：FIREFOX，CHROME，SAFARI，IE，PHANTOMJS
        driver='I:\Softs\Google\Chrome\Application'                  # 驱动程序路径，firefox不需要
    )
    crawler.start()

