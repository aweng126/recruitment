# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ZhiweiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #公司名称
    gsmc=scrapy.Field()
    #职位名称
    zwmc=scrapy.Field()
    #招聘人数
    zprs=scrapy.Field()
    #职位月薪
    zwyx= scrapy.Field()
    #公司地点
    gsdd = scrapy.Field()
    #学历要求
    xlyq=scrapy.Field()
    #经验要求
    jyyq=scrapy.Field()
    #职位描述
    gwms=scrapy.Field()
    #职位类别
    zwlb=scrapy.Field()
    # 信息来源
    xxly = scrapy.Field()

class TongchengItem(scrapy.Item):

    #公司名称
    gsmc=scrapy.Field()
    #职位名称
    zwmc=scrapy.Field()
    #招聘人数
    zprs=scrapy.Field()
    #职位月薪
    zwyx= scrapy.Field()
    #公司地点
    gsdd = scrapy.Field()
    #学历要求
    xlyq=scrapy.Field()
    #经验要求
    jyyq=scrapy.Field()
    #职位描述
    gwms=scrapy.Field()
    #职位类别
    zwlb=scrapy.Field()
    #信息来源
    xxly=scrapy.Field()