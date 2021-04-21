# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class waitroseItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    amount = scrapy.Field()
    weight = scrapy.Field()


class mandsItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    amount = scrapy.Field()
    weight = scrapy.Field()