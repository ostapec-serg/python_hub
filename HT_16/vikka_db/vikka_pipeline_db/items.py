# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class VikkaPipelineDbItem(scrapy.Item):
    title_name = scrapy.Field()
    news_text = scrapy.Field()
    tags = scrapy.Field()
    news_page_url = scrapy.Field()
    date = scrapy.Field()
