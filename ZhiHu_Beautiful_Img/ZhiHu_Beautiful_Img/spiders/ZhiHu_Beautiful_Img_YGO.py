from scrapy.spiders import Spider
from scrapy import Request
from scrapy.selector import Selector

from .. import settings
from ..items import ZhihuBeautifulImgItem

class ZhiHu_Beautiful_Img_YGO(Spider):
    name = 'ZhiHu_Beautiful_Img_YGO'
    def start_requests(self):
        url = 'https://www.zhihu.com/question/40024684'
        yield Request(url, headers=self.headers)