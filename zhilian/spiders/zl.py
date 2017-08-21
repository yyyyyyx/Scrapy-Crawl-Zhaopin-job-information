# -*- coding: utf-8 -*-

import scrapy
import re
from bs4 import BeautifulSoup
from scrapy.http import Request
from zhilian.items import ZhilianItem

class ZlSpider(scrapy.Spider):
    name = 'zl'
    allowed_domains = ['sou.zhaopin.com']
    first_url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=全国&sm=0&p='
    last_url = '&sg=d5859246414f499ba3fa6c723a9749f5'
    def start_requests(self):
        for i in range(1,91):
            url = self.first_url + str(i) + self.last_url
            yield Request(url,self.parse)

    def parse(self, response):
        soup = BeautifulSoup(response.body.decode('utf-8'),'lxml')
        for site in soup.find_all('table',class_='newlist'):
            item = ZhilianItem()
            try:
                item['name'] = site.find('td',class_='zwmc').get_text().strip()
                #print(item['name'])
                item['rate'] = site.find('td',class_='fk_lv').get_text()
                #print(item['rate'])
                item['compy'] = site.find('td',class_='gsmc').get_text()
                #print(item['compy'])
                item['money'] = site.find('td',class_='zwyx').get_text()
                #print(item['money'])
                item['place'] = site.find('td',class_='gzdd').get_text()
                #print(item['place'])
                #print(item)
                yield item
            except:
                pass