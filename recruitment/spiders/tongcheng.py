# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from recruitment.items import TongchengItem

class TongchengSpider(scrapy.Spider):
    handle_httpstatus_list = [301, 302]
    name = 'tongcheng'
    allowed_domains = ['58.com']
    didian_list={'bj','cd','cq','cs','cc','dl','dg','fz','fs','gz',
          'gy','gl','hz','hz','heb','hf','hhht','hk','jn','km',
           'lz','ls','nj','nb','nn','nc','qd','sh','sz',
          'sy','sjz','sz','tj','ty','wh','wx','wlmq','wh',
          'xa','xm','xn','yc','yc','yt','zz','zh'}
    # tongcheng_url='http://jn.58.com/tech/pn1/?utm_source=market&spm=b-31580022738699-me-f-824.bdpz_biaoti&PGTID=0d303655-0010-915b-ca53-cb17de8b2ef6&ClickID=3'
    tongcheng_url='http://{dd}.58.com/tech/'

    num = 0

    def start_requests(self):
        for didian in self.didian_list:
            yield Request(self.tongcheng_url.format(dd=didian), self.parse_per_page)

    def parse_per_page(self, response):

         url_list = response.css('.main .leftbar .infolist dt a::attr(href)').extract()
         if not url_list:
             url_list = response.css('.main .leftCon li .job_name  a::attr(href)').extract()

         if not url_list:
             print('url list 为空')

         for tongcheng_per_message_url in url_list:
             yield Request(url=tongcheng_per_message_url, callback=self.parse_per_message)
         #下一界面的链接
         tongcheng_next_page = response.css('.main .leftbar .pagerout .next::attr(href) ').extract_first()
         if not tongcheng_next_page:
             tongcheng_next_page = response.css('.con .main .leftCon .pagesout .next::attr(href) ').extract_first()

         if tongcheng_next_page:
            yield Request(url=tongcheng_next_page, callback=self.parse_per_page)

    def parse_per_message(self, response):
        # print('11111111111',response.status)
        if response.css('.con'):
            #公司地点
            gsdd = response.css('.con  .leftCon .pos_info .pos-area .pos_area_item::text ').extract_first().strip()
            #公司名称
            gsmc= response.css('.con .rightCon .item_con .company_baseInfo .comp_baseInfo_title .baseInfo_link a::text').extract_first().strip()
            #岗位描述
            gwms_arr=response.css('.con .leftCon .item_con .pos_description .posDes .des::text').extract()

            gwms= ''.join(gwms_arr).strip()
            #职位类别
            zwlb = response.css('.con .leftCon .item_con  .pos_base_info .pos_title::text').extract_first().strip()
            #职位月薪
            zwyx = response.css('.con .leftCon .item_con  .pos_base_info .pos_salary::text').extract_first().strip()
            # 职位名称
            zwmc = response.css('.con .leftCon .item_con  .pos_name::text').extract_first().strip()
            condition = response.css('.con .leftCon .item_con  .pos_base_condition .item_condition::text').extract()
            #招聘人数
            zprs = condition[0].strip()
            #学历要求
            xlyq = condition[1].strip()
            #经验要求
            jyyq = condition[2].strip()
            item=TongchengItem()
            item['gsmc'] = gsmc
            item['zwmc'] = zwmc
            item['zprs'] = zprs
            item['zwyx'] = zwyx
            item['gsdd'] = gsdd
            item['xlyq'] = xlyq
            item['jyyq'] = jyyq
            item['gwms'] = gwms
            item['zwlb'] = zwlb
            item['xxly'] = '58同城'
            # print(self.num, item)
            # self.num = self.num + 1
            yield item
