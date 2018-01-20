# -*- coding: utf-8 -*-
import scrapy
from tutorial.url_items import FoodItem
from tutorial.url_items import CalorieItem
import re


class FoodSpider(scrapy.Spider):
    name = 'food'
    allowed_domains = ['www.boohee.com']
    start_urls = ['http://www.boohee.com/food']
    header = {}
    base_url = "http://www.boohee.com"

    def start_requests(self):

        for url in self.start_urls:
            yield scrapy.Request(url=url, headers=self.header, method='GET', callback=self.calorie_parse)

    def calorie_parse(self, response):
        cate = response.xpath('//ul[@class="row"]/li')
        if cate:
            for child in cate:
                item = FoodItem()
                item['url'] = child.xpath('.//div[@class="img-box"]/a/@href').extract_first()
                item['name'] = child.xpath('.//div[@class="text-box"]//h3/a/text()').extract_first()
                url = self.base_url+item["url"]

                yield scrapy.Request(url=url, headers=self.header, method='GET', callback=self.parse)
                print(url)
                # yield item

    def parse(self, response):
        print("success+")
        li = response.xpath('//ul[@class="food-list"]/li')
        if li:
            for child in li:
                item = CalorieItem()
                content = child.xpath('.//div[@class="text-box pull-left"]/h4/a/text()').extract_first()
                m = re.match(r'(.*)，又叫(.*)', content)
                if m:
                    name = m.group(1)
                    alias = m.group(2)
                    alias1 = alias.replace('...', '')
                    alias2 = re.split(r'，', alias1)
                else:
                    name = content
                    alias2 = ''
                item['name'] = name
                item['alias'] = ','.join(alias2)
                item['calorie'] = child.xpath('.//div[@class="text-box pull-left"]/p/text()').re(r'.*?[：:]\s*?(\d+)')[0]
                item['detail_url'] = self.base_url + child.xpath('.//div[@class="text-box pull-left"]/h4/a/@href').extract_first()
                yield item
        next_url = response.xpath('//a[@class="next_page"]/@href').extract_first()
        if next_url:
            yield scrapy.Request(url=self.base_url+next_url, callback=self.parse)




