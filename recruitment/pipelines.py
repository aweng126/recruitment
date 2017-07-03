# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.exceptions import DropItem
from openpyxl import Workbook

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

    collection_name = 'zhilian'

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
        self.db[self.collection_name].insert_one(dict(item))
        return item

class TuniuPipeline(object):  # 设置工序一
    wb = Workbook()
    ws = wb.active
    ws.append(['职位名称', '职位类别', '职位月薪', '学历要求', '经验要求', '招聘人数', '工作地点', '公司名称', '职位描述'])  # 设置表头、

    def process_item(self,item,spider):
        line = [item['zwmc'], item['zwlb'], item['zwyx'], item['xlyq'], item['jyyq'], item['zprs'], item['gsdd'],
                item['gsmc'],item['gwms']]  # 把数据中每一项整理出来
        self.ws.append(line)
        self.wb.save('hhh.xlsx')
        # print(line)
