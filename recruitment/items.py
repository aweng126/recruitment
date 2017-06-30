# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhilianItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #职位名称
    zwmc=scrapy.Field()
    #职位月薪
    zwyx= scrapy.Field()
    #公司地点
    gsdd = scrapy.Field()
    #招聘数量
    zprs=scrapy.Field()
