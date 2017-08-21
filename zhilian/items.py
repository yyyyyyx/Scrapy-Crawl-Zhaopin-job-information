# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhilianItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()#职位名称
    rate = scrapy.Field()#反馈率
    compy = scrapy.Field()#公司
    money = scrapy.Field()#月薪
    place = scrapy.Field()#工作地点
    
