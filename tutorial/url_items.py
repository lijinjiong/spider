import scrapy


class FoodItem(scrapy.Item):
    # 类别url
    url = scrapy.Field()
    name = scrapy.Field()


class CalorieItem(scrapy.Item):
    # 类别url
    name = scrapy.Field()
    alias = scrapy.Field()
    calorie = scrapy.Field()
    detail_url = scrapy.Field()
