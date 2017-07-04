# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from recruitment.items import TongchengItem

class TongchengSpider(scrapy.Spider):
    name = 'tongcheng'
    allowed_domains = ['jn.58.com']
    tongcheng_url='http://jn.58.com/tech/pn1/?utm_source=market&spm=b-31580022738699-me-f-824.bdpz_biaoti&PGTID=0d303655-0010-915b-ca53-cb17de8b2ef6&ClickID=3'
    num = 0

    def start_requests(self):
        yield Request(self.tongcheng_url, self.parse_per_page)

    def parse_per_page(self, response):
         url_list = response.css('.main .leftbar .infolist dt a::attr(href)').extract()
         if not url_list:
             url_list = response.css('.main .leftCon li .job_name  a::attr(href)').extract()
         if not url_list:
             print('url list 为空')

         for tongcheng_per_message_url in url_list:
             yield Request(url=tongcheng_per_message_url, callback=self.parse_per_message)
         #下一界面的链接
         tongcheng_next_page= response.css('.main .leftbar .pagerout .next::attr(href) ').extract_first()
         # if tongcheng_next_page:
         #       yield Request(url=tongcheng_next_page, callback=self.parse_per_page)

         response.css('.main .leftCon .pagesout .next::attr(href) ').extract_first()

    def parse_per_message(self, response):

        #工作地点
        gzdd = response.css('.con  .leftCon .pos_info .pos-area .pos_area_item::text ').extract_first()

        #公司名称
        gsmc= response.css('.con .rightCon .item_con .company_baseInfo .comp_baseInfo_title .baseInfo_link a::text').extract_first()

        #职位描述
        zwms=response.css('.con .leftCon .item_con .pos_description .posDes .des::text').extract_first()

        #职位类别
        zwlb = response.css('.con .leftCon .item_con  .pos_base_info .pos_title::text').extract_first()
        #职位月薪
        zwyx = response.css('.con .leftCon .item_con  .pos_base_info .pos_salary::text').extract_first()
        # 职位名称
        zwmc = response.css('.con .leftCon .item_con  .pos_name::text').extract_first()

        condition = response.css('.con .leftCon .item_con  .pos_base_condition .item_condition::text').extract()

        #招聘人数
        zprs = condition[0]
        #学历限制
        xlyq = condition[1]
        #经验限制
        jyyq = condition[2]

        print(zwlb,zwyx,zwmc,zprs,xlyq,jyyq)

        # pass