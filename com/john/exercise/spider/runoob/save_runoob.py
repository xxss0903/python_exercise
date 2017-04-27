#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib
import urllib2
import sys
from os import path

import time

import zlib
import gzip, StringIO

from pip.utils import logging
from selenium import webdriver


def openpage():
    url = 'http://www.runoob.com/python/python-files-io.html'
    request = urllib2.Request(url)
    request.add_header('Accept-encoding', 'gzip')
    opener = urllib2.build_opener()
    response = opener.open(request)
    html = response.read()
    gzipped = response.headers.get('Content-Encoding')
    if gzipped:
        html = zlib.decompress(html, 16+zlib.MAX_WBITS)
    # print html

    # 获取侧栏文章导航内容
    browser = webdriver.Chrome()
    browser.get(url)
    indexes = browser.find_elements_by_css_selector('#leftcolumn a')
    idx = 1
    # for index in indexes:
    #     # 保存网页内容
    #     print  '教程序列',idx,'=',index.text,'href=',index.get_attribute('href')
    #     idx+=1
    # browser.quit()
    return indexes


def download(url, save_path):
    print '下载的url =', url
    try:
        with open(save_path, 'wb') as fp:
            request = urllib2.Request(url)
            request.add_header('Accept-encoding', 'gzip')
            opener = urllib2.build_opener()
            response = opener.open(request)
            html = response.read()
            gzipped = response.headers.get('Content-Encoding')
            if gzipped:
                html = zlib.decompress(html, 16 + zlib.MAX_WBITS)

            # print html

            fp.write(html)
    except Exception, et:
        logging.error(et, exc_info=True)
        logging.error('cannot download: %s' % url)
    pass


indexes = openpage()
print indexes
save_folder="D:\\python\\runoob"
idx=1
for index in indexes:
    href = index.get_attribute('href')
    name=index.text
    name = name.replace("/","_")
    # name.replace(" ","")
    # save_img_path = path.join(save_folder,
    #                           ('%03d' % img_idx) + '.' + path.basename(url).split('.')[-1])
    # save_path = path.join(save_folder, ('%03d' % idx)) + '.html'
    save_path = save_folder + "\\" + name + '.html'
    print save_path
    # save_path=save_folder+"\\"+'page_'+'.html'

    # print save_path
    download(href,save_path)
    idx+=1
    pass




