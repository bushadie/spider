# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.exceptions import DropItem
# 需要导入ImagesPipeline
from scrapy.pipelines.images import ImagesPipeline
import settings
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class ZhihuBeautifulImgPipeline(object):
    # 用get_media_requests方法进行下载控制，返回一个requests对象
    # 对象被Pipeline处理，下载结束后，默认直接将结果传给item_completed方法
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['ImgUrl'])
        pass

    def item_completed(self, results, item, info):
        path = [x['path'] for ok, x in results if ok]
        if not path:
            raise DropItem('Item contains no images')
        print u'正在保存图片', item['ImgUrl']
        return item
        pass

    def process_item(self, item, spider):
        return item
