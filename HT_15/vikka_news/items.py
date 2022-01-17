# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class VikkaNewsItem(scrapy.Item):
    # define the fields for your item here like:
    title_name = scrapy.Field()
    news_text = scrapy.Field()
    tags = scrapy.Field()
    news_page_url = scrapy.Field()
