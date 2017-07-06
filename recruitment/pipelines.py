# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.exceptions import DropItem
from openpyxl import Workbook

class SalaryFormatPipline(object):
    def hasNumbers(self,inputString):
        return any(char.isdigit() for char in inputString)

    def addYuan(self,inputstring):
        lists = inputstring.split('-')
        aa = ''
        for list in lists:
            list += '元-'
            aa += list
        return aa[:-1]

    def process_item(self, item, spider):
        if self.hasNumbers(item['zwyx']):
            item['zwyx']=self.addYuan(item['zwyx'])
        # print(item)
        return item

class DuplicatesPipeline(object):

    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        if item['id'] in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(item['id'])
            return item


class MongoPipeline(object):

    collection_name = 'tongcheng'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        print('process_item',dict(item))
        self.db[self.collection_name].insert_one(dict(item))
        return item

class TuniuPipeline(object):  # 设置工序一
    wb = Workbook()
    ws = wb.active
    ws.append(['job_name', 'job_class', 'job_wages', 'job_acquire', 'job_exper', 'job_num', 'com_place', 'com_name', 'com_intro','job_sourse'])  # 设置表头、

    def process_item(self,item,spider):
        line = [item['zwmc'], item['zwlb'], item['zwyx'], item['xlyq'], item['jyyq'], item['zprs'], item['gsdd'],
                item['gsmc'],item['gwms'],item['xxly']]  # 把数据中每一项整理出来
        self.ws.append(line)
        self.wb.save('tongcheng.xlsx')
        # print(line)
