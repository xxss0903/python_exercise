import urllib
import urllib2

url = 'http://tw.ikanman.com/comic/4740/184715.html#p=3'

response = urllib2.urlopen(url)
html = response.read()
print html