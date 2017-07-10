from scrapy.spiders import Spider
from scrapy import Request
from scrapy.selector import Selector
import scrapy

from .. import settings
from ..items import ZhihuBeautifulImgItem


class ZhiHu_Beautiful_Img_YGO(Spider):
    name = 'ZhiHu_Beautiful_Img_YGO'


    def start_requests(self):
        url = 'https://www.zhihu.com/question/40024684'
        yield Request(url)

    def parse(self, response):
        item = ZhihuBeautifulImgItem()
        imgs = response.xpath(
            '//div[@class="List-item"]//img/@src')
        for img in imgs:
            try:
                item['ImgUrl'] = img.extract()
                if 'jpg' in item['ImgUrl']:
                    continue
                yield item
                pass
            except:
                print '--------------error--------------'
                pass
