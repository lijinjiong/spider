from tutorial.items import DoubanMovieItem
import scrapy
from lxml import etree


class DoubanMovieTop250Spider(scrapy.Spider):
    name = 'douban_movie_top250'
    start_urls = ['https://movie.douban.com/top250']
    allowed_domains = ['movie.douban.com']

    def start_requests(self):
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 \
                      Safari/537.36 SE 2.X MetaSr 1.0'
        headers = {'User-Agent': user_agent}
        for url in self.start_urls:
            yield scrapy.Request(url=url, headers=headers, method='GET', callback=self.parse)

    def parse(self, response):
        item = DoubanMovieItem()
        movies = response.xpath('//ol[@class="grid_view"]/li')
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 \
                            Safari/537.36 SE 2.X MetaSr 1.0'
        headers = {'User-Agent': user_agent}
        for movie in movies:

            item['ranking'] = movie.xpath(
                './/div[@class="pic"]/em/text()')   .extract()[0]
            item['movie_name'] = movie.xpath(
                './/div[@class="hd"]/a/span[1]/text()').extract()[0]
            item['score'] = movie.xpath(
                './/div[@class="star"]/span[@class="rating_num"]/text()'
            ).extract()[0]
            item['score_num'] = movie.xpath(
                './/div[@class="star"]/span/text()').re(u'(\d+)人评价')[0]
            yield item
        next_urls = response.xpath('//span  [@class="next"]/a/@href').extract()
        if next_urls:
            next_url = 'https://movie.douban.com/top250'+next_urls[0]
            yield scrapy.Request(url=next_url, headers=headers)
    