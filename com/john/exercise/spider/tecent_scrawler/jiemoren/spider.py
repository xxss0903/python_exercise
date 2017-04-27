# -*- coding: utf-8 -*-
import os
import urllib
import urllib2

import logging

from os import path

import time
from selenium import webdriver


class Spider:
    def __init__(self, site, begin=0, end=-1, save_folder="G:\Cartoon\tencent"):
        self.__site = site
        self.__begin = begin
        self.__end = end
        self.__save_folder = save_folder

    def read_html(self):
        response = urllib2.urlopen(self.__site)
        html = response.read()
        return html

    def open_browser(self):

        self.__bro = webdriver.Chrome()
        self.__bro.set_window_size(1000, 3000000)
        self.__bro.get(self.__site)

        self.get_catagolue_list()

    def get_catagolue_list(self):
        # 获取漫画章节信息，多少话
        catalogue_list = self.__bro.find_elements_by_css_selector('#catalogueListWrap ul li a')
        catalogue_idx = 1
        for catalogue in catalogue_list:
            print '------------开始第', catalogue_idx, ' 话'
            catalogue_url = catalogue.get_attribute('href')
            self.download_catalogue(catalogue_url, catalogue_idx)
            print '------------下载完第', catalogue_idx, ' 话'
            catalogue_idx = catalogue_idx + 1

    def download_catalogue(self, catalogue_url, catalogue_idx):
        if not path.exists(self.__save_folder):
            os.mkdir(self.__save_folder)

        folder_name = self.__bro.find_element_by_class_name('title-comicHeading').text
        print 'class-name =', folder_name
        save_folder = self.__save_folder + folder_name

        if not path.exists(save_folder):
            os.mkdir(save_folder)

        print '保存', save_folder


        # 获取每话的图片链接，然后进行保存
        self.__bro.get(catalogue_url)
        time.sleep(1)

        self.__bro.execute_script("document.documentElement.scrollTop=50000")
        time.sleep(5)
        self.__bro.execute_script("document.documentElement.scrollTop=5000")
        time.sleep(5)

        print '开始滑动滑动界面'
        js = 'document.getElementsByClassName("main")[0].scrollTop=10000'
        # 就是这么简单，修改这个元素的scrollTop就可以
        self.__bro.execute_script(js)

        time.sleep(10)

        catalogue_content_list = self.__bro.find_elements_by_css_selector('#mainView ul li img')
        img_idx = 0
        for content in catalogue_content_list:
            print "图片地址 =", content.get_attribute('src')
            # img_idx = img_idx + 1
            # url = content.get_attribute('src')
            # print '图片地址', url
            # save_img_path = path.join(save_folder,
            #                           ('%03d' % img_idx) + '.' + path.basename(url).split('.')[-1])
            # print '保存图片地址', save_img_path
            #
            # self.download(url, save_img_path)
            # pass
        pass

    #         下载页面
    def download(self, url, save_path):
        print '下载的url =', url
        try:
            with open(save_path, 'wb') as fp:
                fp.write(urllib.urlopen(url).read())
        except Exception, et:
            logging.error(et, exc_info=True)
            logging.error('cannot download: %s' % url)

        pass

    def __del__(self):
        self.__bro.quit()

        pass
