# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.conf import settings
import pymongo

class ZufangPipeline(object):
    def process_item(self, item, spider):
        return item

class AnjukeMongoPipeline(object):
    def __init__(self):
        # 获取setting主机名、端口号和数据库名
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbname = settings['MONGODB_DBNAME']
        # pymongo.MongoClient(host, port) 创建MongoDB链接
        self.client = pymongo.MongoClient(host=host, port=port)
        # 指向指定的数据库
        self.mdb = self.client[dbname]
        # 获取数据库里存放数据的表名
        self.table = self.mdb[settings['MONGODB_DOCNAME']]

    def process_item(self, item, spider):
        data = dict(item)
        self.table.insert(data)
        return item

    def __del__(self):
        self.client.close()
