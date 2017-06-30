# -*- coding: utf-8 -*-
import logging

import scrapy
from scrapy import Request

from recruitment.items import ZhilianItem


class ZhilianSpider(scrapy.Spider):
    name = 'zhilian'
    allowed_domains = ['www.zhaopin.com']
    start_urls = ['http://www.zhaopin.com/']

    zhilian_url='http://sou.zhaopin.com/jobs/searchresult.ashx?in=210500%3B160000%3B160200&jl=%E5%8C%97%E4%BA%AC&p=1&isadv=0'

   # response.css('.newlist .zwyx::text ').extract()

    def start_requests(self):
        yield  Request(self.zhilian_url,self.parse_zhilian)

    def parse_zhilian(self,response):
        lists=response.css('.newlist')

        for list in lists[1:]:

            item=ZhilianItem()

            zwmc = list.css('.zwmc  div a::text').extract_first() #职位名称z
            zwyx = list.css('.zwyx::text').extract_first()   # 职位月薪
            gsdd = list.css('.gzdd::text').extract_first()  # 公司地点

            # 招聘数量 (这里是一个url,想要的招聘人数在这个网址中)
            zprs = list.css('.zwmc div a::attr(href)')
            item['zwyx'] = zwyx
            item['zwmc'] = zwmc
            item['gsdd'] = gsdd
            print(item)
            yield  item





