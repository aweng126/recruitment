# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

from recruitment.items import ZhiweiItem


class ZhaopinSpider(scrapy.Spider):
    name = 'zhaopin'
    allowed_domains = ['zhaopin.com']

    num = 1
    #一期数据爬取
    list_city  = {'济南','北京','成都','重庆','长沙','长春','大连'}

    #二期数据爬取
    list_city2 = {'东莞','福州','佛山','广州','贵阳','桂林',
                 '杭州','惠州','哈尔滨','合肥','呼和浩特','海口','昆明','兰州','拉萨','南京','宁波','南宁',
                 '南昌','青岛','上海','深圳','沈阳','石家庄','苏州','天津','太原','武汉','乌鲁木齐','无锡',
                 '威海','西安','厦门','西宁','银川','宜昌','烟台','郑州','珠海'}

    zhilian_url='http://sou.zhaopin.com/jobs/searchresult.ashx?in=210500%3B160000%3B160200&jl={city}&p=1&isadv=0'

    def start_requests(self):
        for mcity in self.list_city:
            yield Request(self.zhilian_url.format(city=mcity), self.parse_page)

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
        gsmc = response.css('.top-fixed-box .fixed-inner-box  .fl h2 a::text').extract_first()

        #职位名称
        zwmc = response.css('.top-fixed-box .fixed-inner-box  .fl h1::text').extract_first()

        #职位描述
        zwms_array = response.css('.terminalpage-main .tab-cont-box  .tab-inner-cont div p span::text ').extract()
        if not zwms_array:
            zwms_array=response.css('.terminalpage-main .tab-cont-box  .tab-inner-cont div p::text ').extract()
        if not zwms_array:
            zwms_array = response.css('.terminalpage-main .tab-cont-box  .tab-inner-cont p span::text ').extract()
        if not zwms_array:
            zwms_array = response.css('.terminalpage-main .tab-cont-box  .tab-inner-cont p::text ').extract()
        zwms = ''.join(zwms_array).strip().replace('/t', '')

        #公司地点
        gsdd = response.css('.terminalpage-main .tab-cont-box h2::text').extract_first().strip()[:3]

        #职位类别
        zwlb=response.css('.terminalpage  .terminalpage-left .terminal-ul li strong a::text').extract()[1]
        #信息来源
        xxly='智联招聘'

        item =ZhiweiItem()
        item['gsmc']=gsmc
        item['zwmc']=zwmc
        item['zprs']=zprs
        item['zwyx']=zwyx
        item['gsdd']=gsdd
        item['xlyq']=xlyq
        item['jyyq']=jyyq
        item['gwms']=zwms
        item['zwlb']=zwlb
        item['xxly']=xxly
        yield item

        self.num=self.num+1

