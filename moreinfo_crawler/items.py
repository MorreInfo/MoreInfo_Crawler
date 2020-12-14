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

class DouBanBookSearchItem(scrapy.Item):
    cover_url = scrapy.Field()
    score = scrapy.Field()
    score_num = scrapy.Field()
    url = scrapy.Field()
    abstract = scrapy.Field()
    title = scrapy.Field()
    id = scrapy.Field()

class DoubanBook250Item(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    cover_url = scrapy.Field()
    # orginal_title = scrapy.Field()
    author = scrapy.Field()
    publisher = scrapy.Field()
    # release_time = scrapy.Field()
    # price = scrapy.Field()
    score = scrapy.Field()
    score_num = scrapy.Field()
    simple_comment = scrapy.Field()


