# -*-coding:utf-8 -*-


import sys
import requests
import random
import re
import cookielib
reload(sys)
sys.setdefaultencoding('utf-8')


class Spider():
    def __init__(self):
        pass

    def getSource(self, url):
        session = requests.session()
        session.cookies = cookielib.LWPCookieJar(filename='cookies')
        try:
            session.cookies.load(ignore_discard=False)
        except:
            print "Cookie 未能加载"

        user_agents = ['Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20130406 Firefox/23.0',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0',
                       'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533+ \(KHTML, like Gecko) Element Browser 5.0',
                       'IBM WebExplorer /v0.94', 'Galaxy/1.0 [en] (Mac OS X 10.5.6; U; en)',
                       'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
                       'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14',
                       'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) \Version/6.0 Mobile/10A5355d Safari/8536.25',
                       'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) \Chrome/28.0.1468.0 Safari/537.36',
                       'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0; TheWorld)']
        # user_agent在一堆范围中随机获取
        # random.randint()获取随机数，防止网站认出是爬虫而访问受限
        index = random.randint(0, 9)
        user_agent = user_agents[index]
        headers = {'User_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'}
        html = requests.get(url, headers=headers)
        return html.text

    def Satrt(self):
        url = 'https://www.zhihu.com/question/40024684'
        html = self.getSource(url=url)
        print html
        # pattern = re.compile(r'')

        pass


spider = Spider()
spider.Satrt()
