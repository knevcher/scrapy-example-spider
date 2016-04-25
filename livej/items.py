# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LivejItem(scrapy.Item):

    title = scrapy.Field()
    content = scrapy.Field()
    #tags = scrapy.Field()
    link = scrapy.Field()
    #date = scrapy.Field()
    image_paths = scrapy.Field()


class ImageItem(scrapy.Item):

    src = scrapy.Field()
