# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
from scrapy.conf import settings
class LianjiaPipeline(object):
    def __init__(self):
        # 链接数据库
        self.client = MongoClient(host=settings['MONGO_HOST'],port=settings['MONGO_PORT'])
        # 数据库登录需要帐号密码的话
        # self.client.admin.authenticate(settings['MINGO_USER'], settings['MONGO_PSW'])
        self.db = self.client[settings['MONGO_DB']] # 获得数据库的句柄
        self.coll = self.db[settings['MONGO_COLL']] # 获得collection的句柄

    def process_item(self, item, spider):
        db_item = dict(item)
        self.coll.insert(db_item)
        return item
