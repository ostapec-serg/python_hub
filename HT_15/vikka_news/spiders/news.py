import scrapy

from vikka_news.items import VikkaNewsItem

from datetime import datetime

import csv


class NewsSpider(scrapy.Spider):

    name = 'news'
    allowed_domains = ['vikka.ua']
    start_urls = ['http://vikka.ua/']
    parse_date = None

    def start_requests(self):
        """
        start_request method called automatically.
        Accepts from the user the date on which to search for news.
        Calls a request for vikka.ua + the specified date,
        the result is sent for processing to the method
        parse_date_page
         """
        parse_date = input("Select date to parse. "
                           "Use format(%Y/%m/%d) "
                           "for example(2022/01/14)"
                           "(today for default):\n"
                           )
        parse_date = parse_date or datetime.today().strftime("%Y/%m/%d")
        if self.date_checking(parse_date):
            parse_url = NewsSpider.start_urls[0]+parse_date
            self.parse_date = f"{parse_date.replace('/', '_')}.csv"
            with open(self.parse_date, 'w+', encoding='utf-8') as file:
                fieldnames = [
                    'title_name',
                    'news_text',
                    'tags',
                    'news_page_url'
                ]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
            yield scrapy.Request(
                url=parse_url,
                callback=self.parse_date_page,
            )

    def parse_date_page(self, response):
        """
        The method accepts the response to the request in the method
        start_requests and consists of all news for the date specified
        by the user. The method collects all links to each separate
        news item and passes them into the parse_page_info method
        to extract the necessary data
        """
        container = response.css('.item-cat-post')
        print(container)
        for links in container:
            link = links.css('a::attr(href)').get()
            yield response.follow(link, callback=self.parse_page_info)

    def parse_page_info(self, page_response):
        """
        The method processes links to news. Extracts the necessary data
        and writes them to a csv file with a name corresponding to the
        date on which the news is selected
        """
        item = VikkaNewsItem()
        tag_list = ""
        news_info = ""
        for tag in page_response.css('a.post-tag::text').getall():
            tag_list += f"#{tag} "
        for text in page_response.css('div.entry-content > p::text').getall():
            news_info += text.replace(u'\xa0', ' ')
        item['title_name'] = page_response.css('h1.post-title::text').get()
        item['news_text'] = news_info
        item['tags'] = tag_list
        item['news_page_url'] = page_response.url
        with open(self.parse_date, 'a', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=list(item.keys()))
            writer.writerow(item)

    def date_checking(self, parse_date):
        """ date_checking method """
        date_news = parse_date
        time_now = datetime.today()
        date = datetime.strptime(date_news, "%Y/%m/%d")
        if date <= time_now and len(date_news) == 10:
            return True
        else:
            return False
    # 2022/01/14
    # 2022.01.14
