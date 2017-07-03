# -*- coding: utf-8 -*-
import logging

import scrapy
from scrapy import Request

from recruitment.items import ZhilianItem


class ZhilianSpider(scrapy.Spider):
    name = 'zhilian'
    allowed_domains = ['sou.zhaopin.com']

    num = 1

    zhilian_url='http://sou.zhaopin.com/jobs/searchresult.ashx?in=210500%3B160000%3B160200&jl=%E5%8C%97%E4%BA%AC&p=1&isadv=0'


    def start_requests(self):
        yield  Request(self.zhilian_url, self.parse_zhilian)

    def parse_zhilian(self, response):
        lists=response.css('.newlist')

        for list in lists[1:]:
            item = ZhilianItem()
            zwmc = list.css('.zwmc  div a::text').extract_first() #职位名称
            zwyx = list.css('.zwyx::text').extract_first()   # 职位月薪
            gsdd = list.css('.gzdd::text').extract_first()  # 公司地点

            # 招聘数量 (这里是一个url,想要的招聘人数在这个网址中)
            zprs_url = list.css('.zwmc div a::attr(href)').extract_first()
            yield Request(url=zprs_url,callback=self.parse_zprs)

            # print(self.num, zprs_url)

            # item['zwyx'] = zwyx
            # item['zwmc'] = zwmc
            # item['gsdd'] = gsdd
            # item['zprs']
            # print(self.num, item)

            self.num = self.num+1
            yield item

        # next_page = response.css('.pagesDown-pos  a::attr(href)').extract_first()
        # print('1111111111', next_page)

        # if next_page:
        #     yield Request(url=next_page, callback=self.parse_zhilian)

    def parse_zprs(self, response):
        print('1111111111', response.text)


