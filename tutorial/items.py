# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

# import scrapy
#
#
# class TutorialItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#
import scrapy


class  DmozItem(scrapy.Item):
    author = scrapy.Field()
    text = scrapy.Field()
    # desc = scrapy.Field()


class DoubanMovieItem(scrapy.Item):
        # 排名
        ranking = scrapy.Field()
        # 电影名称
        movie_name = scrapy.Field()
        # 评分
        score = scrapy.Field()
        # 评论人数
        score_num = scrapy.Field()


class WeiboSpiderItem(scrapy.Item):
    # 排名
    ranking = scrapy.Field()
    # 电影名称
    movie_name = scrapy.Field()
    # 评分
    score = scrapy.Field()
    # 评论人数
    score_num = scrapy.Field()
