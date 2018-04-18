# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from openpyxl import Workbook

class JdPipeline(object):
    def __init__(self):
       #self.wb = load_workbook("jd.xlsx")
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.title='jd'

    def process_item(self, item, spider):
        self.ws.append([str(item["name"]),str(item["price"])])
        self.wb.save("jd.xlsx")
        return item
