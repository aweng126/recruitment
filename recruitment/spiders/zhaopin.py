# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

from recruitment.items import ZhilianItem


class ZhaopinSpider(scrapy.Spider):
    name = 'zhaopin'
    allowed_domains = ['zhaopin.com']

    num = 1

    zhilian_url='http://sou.zhaopin.com/jobs/searchresult.ashx?in=210500%3B160000%3B160200&jl=%E5%8C%97%E4%BA%AC&p=1&isadv=0'


    def start_requests(self):
        yield Request(self.zhilian_url, self.parse_page)

    def parse_page(self,response):
        per_page_url_lists=response.css('.newlist')[1:]

        for list in per_page_url_lists:
             url_per_zhaopin =list.css('.zwmc div a::attr(href)').extract_first()

             yield  Request(url=url_per_zhaopin,callback=self.parse_per_zhaopin)

        next_page = response.css(' .pagesDown-pos  a::attr(href)').extract_first()
        yield Request(url=next_page, callback=self.parse_page)


    def parse_per_zhaopin(self,response):
        yq_array=response.css('.terminalpage  .terminalpage-left .terminal-ul li strong::text').extract()
        #职位月薪
        zwyx=yq_array[0][:-4]
        #招聘人数
        zprs=yq_array[-1][:-2]
        #学历要求
        xlyq=yq_array[-2]
        #经验要求
        jyyq=yq_array[-3]

        #公司名称
        gsmc = response.css('.top-fixed-box .fixed-inner-box  .fl h2 a::text').extract()

        #职位名称
        zwmc = response.css('.top-fixed-box .fixed-inner-box  .fl h1::text').extract()

        #职位描述
        zwms_array = response.css('.terminalpage-main .tab-cont-box  .tab-inner-cont div p span::text ').extract()
        if not zwms_array:
            zwms_array=response.css('.terminalpage-main .tab-cont-box  .tab-inner-cont div p::text ').extract()
        if not zwms_array:
            zwms_array = response.css('.terminalpage-main .tab-cont-box  .tab-inner-cont p span::text ').extract()
        if not zwms_array:
            zwms_array = response.css('.terminalpage-main .tab-cont-box  .tab-inner-cont p::text ').extract()
        zwms = ''.join(zwms_array).strip()

        #公司地点
        gsdd = response.css('.terminalpage-main .tab-cont-box h2::text').extract_first().strip()[:3]

        item =ZhilianItem()
        item['gsmc']=gsmc
        item['zwmc']=zwmc
        item['zprs']=zprs
        item['zwyx']=zwyx
        item['gsdd']=gsdd
        item['xlyq']=xlyq
        item['jyyq']=jyyq
        item['gwms']=zwms
        yield item

        print(self.num,item)
        self.num=self.num+1

