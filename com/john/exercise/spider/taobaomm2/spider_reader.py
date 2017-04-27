import urllib2


class Reader:

    def __init__(self, url):
        self.url = url

    def read(self):
        response = urllib2.urlopen(self.url)
        html = response.read()
        return html