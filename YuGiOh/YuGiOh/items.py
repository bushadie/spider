# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YugiohItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()  # 名字
    lv = scrapy.Field()  # 等级
    atk = scrapy.Field()  # 攻击力
    Def = scrapy.Field()  # 防御力
    effect = scrapy.Field()  # 效果
    attribute = scrapy.Field()  # 属性
    tribe = scrapy.Field()  # 种族
    pass
