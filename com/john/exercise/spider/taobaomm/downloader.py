import urllib2


class Downloader(object):

    def __init__(self, url):
        self.url = url
        pass

    def getHtml(self):
        response = urllib2.urlopen(self.url)
        return response.read()
