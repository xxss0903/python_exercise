# coding:utf-8
import urllib2

import re


class Tool:
    removeImg = re.compile('<img.*?>| {7}|')
    removeAddr = re.compile('<a.*?>|</a>')
    replaceLine = re.compile('<tr>|<div>|</div></p>')
    replaceTD = re.compile('<td>')
    replacePara = re.compile('<p.*?>')
    replaceBR = re.compile('<br><br>|</br>')
    removeExtraTag = re.compile('<.*?>')
    def replace(self, x):
        x = re.sub(self.removeImg, "", x)
        x = re.sub(self.removeAddr, "", x)
        x = re.sub(self.replaceLine, "\n", x)
        x = re.sub(self.replaceTD, "\t", x)
        x = re.sub(self.replacePara, "\n    ", x)
        x = re.sub(self.replaceBR, "\n", x)
        x = re.sub(self.removeExtraTag, "", x)
        return x.strip()

    pass


class BDTB:
    def __init__(self, baseUrl, seeLZ):
        self.baseUrl = baseUrl
        self.seeLZ = seeLZ
        self.tool = Tool()
        pass

    def getPage(self, pageNum):
        try:
            url = self.baseUrl+"seeLZ=" + str(self.seeLZ) + '&pn' + str(pageNum)
            print "url = ", url
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            return response.read()
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print e.reason

    def getTitle(self):
        page = self.getPage(1)
        pattern = re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>', re.S)
        result = re.search(pattern, page)
        print result

        if result:
            return result.group(1).strip()
        else:
            return None
        pass

    def getPageCount(self):
        page = self.getPage(1)
        # pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span class="red">(.*?)</span>', re.S)
        pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>', re.S)
        result = re.search(pattern, page)
        print result.group(1)

        if result:
            return result.group(1).strip()
        else:
            return None
        pass

    def getContent(self, page):
        pageContent = self.getPage(page)
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>', re.S)
        items = re.findall(pattern, pageContent)
        print self.tool.replace(items[1])
        return self.tool.replace(items[1])
        # for item in items:
        #     print item

        pass


baseUrl =  "http://tieba.baidu.com/p/3138733512?"
bdtb = BDTB(baseUrl, 1)

print "---------------"
# print "页面总数",bdtb.getPage(1)
bdtb.getContent(1)
print "---------------"





