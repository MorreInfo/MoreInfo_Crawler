# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class JianShuArticleItem(scrapy.Item):
    article_id = scrapy.Field()
    title = scrapy.Field()
    avatar = scrapy.Field()
    author = scrapy.Field()
    description = scrapy.Field()
    content = scrapy.Field()
    origin_url = scrapy.Field()