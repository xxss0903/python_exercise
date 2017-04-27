
# coding:utf8
import urllib2


class Downloader:
    page = 1
    url = 'http://www.qiushibaike.com/hot/page/' + str(page)

    def __init__(self):
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        Downloader.headers = {'User-Agent': user_agent}


    def readUrl(self):
        try:
            print Downloader.headers
            request = urllib2.Request(Downloader.url, headers=Downloader.headers)
            response = urllib2.urlopen(request)
            return response.read()

        except urllib2.URLError, e:
            if hasattr(e, "code"):
                print e.code
            if hasattr(e, "reason"):
                print e.reason

