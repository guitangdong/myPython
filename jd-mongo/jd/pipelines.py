# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient

class JdPipeline(object):
    def __init__(self, mongo_uri,mongo_port,mongo_database):
        self.mongo_uri = mongo_uri
        self.mongo_port = mongo_port
        self.mongo_database = mongo_database

    def open_spider(self, spider):
        self.client = MongoClient(self.mongo_uri, self.mongo_port)
        self.db = self.client[self.mongo_database]

    def close_spider(self, spider):
        self.client.close()

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_port=crawler.settings.get('MONGO_PORT'),
            mongo_database=crawler.settings.get('MONGO_DATABASE')
        )

    def process_item(self, item, spider):
        self.db.jd.save(item.__dict__)
        return item
