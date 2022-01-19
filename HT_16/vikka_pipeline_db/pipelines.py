# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
import sqlite3


class VikkaPipelineDbPipeline:
    def open_spider(self, spider):
        """ open spider method. connection to database """
        self.table_name = 'data_' + spider.parse_date.replace('/', '_')
        self.con = sqlite3.connect("vikka_news.db")
        self.cursor = self.con.cursor()
        self.creating_table()

    def process_item(self, item, spider):
        """ write item data to database """
        self.cursor.execute(f"""INSERT OR IGNORE INTO {self.table_name}
                            (title_name, news_text, news_tags, news_page_url, 
                            news_date_time) VALUES(?,?,?,?,?)""",
                            (item['title_name'],
                             item['news_text'],
                             item['tags'],
                             item['news_page_url'],
                             item['date']))
        self.con.commit()
        return item

    def creating_table(self):
        """ creating table method """
        self.cursor.execute(f""" CREATE TABLE IF NOT EXISTS {self.table_name}
                            (id INTEGER, 
                            title_name TEXT, 
                            news_text TEXT, 
                            news_tags TEXT, 
                            news_page_url TEXT, 
                            news_date_time TEXT, 
                            PRIMARY KEY(id AUTOINCREMENT))"""
                            )

    def close_spider(self, spider):
        """ close spider. close connection to database """
        self.con.close()
