from scrapy.spiders import Spider
from ..items import YugiohItem
from scrapy import Request

import sys

reload(sys)

sys.setdefaultencoding('utf-8')

class YuGiOhMonsterSpider(Spider):
    name = 'YuGiOhMonsterSpider'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    # start_urls = ['http://www.ourocg.cn/Cards/Lists-1-1']

    def start_requests(self):
        url = 'http://www.ourocg.cn/Cards/Lists-1-2'
        yield Request(url, headers=self.headers)

    def parse(self, response):
        item = YugiohItem()
        cards = response.xpath('//div[@card_id]')
        i = 2
        for card in cards:
            try:
                item['name'] = card.xpath(
                    '//section/div[' + str(i) + ']/div/section/div/h2/a/text()'
                ).extract()[0]
                item['lv'] = card.xpath(
                    '//section/div[' + str(i) + ']/div/section/div/div[1]/span[2]/text()'
                ).extract()[0]
                item['atk'] = card.xpath(
                    '//section/div[' + str(i) + ']/div/section/div/div[1]/span[4]/span[2]/text()'
                ).extract()[0]
                item['Def'] = card.xpath(
                    '//section/div[' + str(i) + ']/div/section/div/div[1]/span[4]/span[4]/text()'
                ).extract()[0]
                item['tribe'] = card.xpath(
                    '//section/div[' + str(i) + ']/div/section/div/div[1]/span[4]/span[6]/text()'
                ).extract()[0]
                item['attribute'] = card.xpath(
                    '//section/div[' + str(i) + ']/div/section/div/div[1]/span[4]/span[8]/text()'
                ).extract()[0]

                effects = card.xpath(
                    '//section/div[' + str(i) + ']/div/section/div/p/text()'
                ).extract()
                item['effect'] = ''
                for effect in effects:
                    item['effect'] += effect
                item['effect'] = item['effect'].replace('\r\n', '')

                print i
                i += 1
                yield item
            except:
                print '-----------------error-------------------------'
        next_url = response.xpath('//*[@id="main"]/div/div/div/section/aside[3]/p/span[3]/a[1]/@href').extract()
        if next_url:
            i = 2
            next_url = 'http://www.ourocg.cn' + next_url[0]
            yield Request(next_url, headers=self.headers)

    pass
