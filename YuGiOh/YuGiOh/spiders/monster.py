from scrapy.spiders import Spider
from ..items import YugiohItem
from scrapy import Request


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
            item['effect'] = card.xpath(
                '//section/div[' + str(i) + ']/div/section/div/p/text()'
            ).extract()[0]

            print i
            i += 1
            yield item

    pass
