# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

from recruitment.items import TongchengItem


class TongchengSpider(scrapy.Spider):
    name = 'tongcheng'
    allowed_domains = ['jn.58.com']
    # start_urls = ['http://jn.58.com/']
    tongcheng_url='http://jn.58.com/tech/pve_5363_245_pve_5358_0/'


    def start_request(self):
        yield Request(url=self.tongcheng_url,callback=self.parse_per_page)

    def parse_per_page(self,response):
        print(response.text)
        #每个具体页面的url
        tongcheng_per_message=''
        yield Request(url=tongcheng_per_message,callback=self.parse_per_message)

        #下一界面的链接
        tongcheng_next_page=''
        yield Request(url=tongcheng_next_page,callback=self.parse_per_page)

    def parse_per_message(self, response):
        item = TongchengItem()
        yield item
