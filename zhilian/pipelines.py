# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os

class ZhilianPipeline(object):
    def open_spider(self, spider):
        path = 'D:/数据/'
        if not os.path.exists(path):
            os.makedirs(path)
        self.file = open(path + '智联招聘.jl', 'wt',encoding='UTF-8')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item),ensure_ascii=False) + '\n'
        self.file.write(line)
        return item
