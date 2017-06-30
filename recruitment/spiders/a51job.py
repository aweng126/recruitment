# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request


class A51jobSpider(scrapy.Spider):
    name = '51job'
    allowed_domains = ['www.51job.com']
    start_urls = ['http://www.51job.com/']

    job_url='http://search.51job.com/list/120200,000000,0000,32,9,99,%2B,2,{page}.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='

    def start_requests(self):
        yield Request(self.job_url.format(page=1),self.parse_recruitment)

    def parse_recruitment(self,response):
        print(response.text)
        response=response.css('.dw_table .')

    # def parse(self, response):
    #     print(response.text)
