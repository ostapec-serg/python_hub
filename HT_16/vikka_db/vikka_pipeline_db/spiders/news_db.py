import scrapy
from datetime import datetime
from vikka_pipeline_db.items import VikkaPipelineDbItem


class NewsDbSpider(scrapy.Spider):
    name = 'news_db'
    allowed_domains = ['vikka.ua']
    start_urls = ['http://vikka.ua/']
    date = input("Select date to parse. "
                 "Use format(%Y/%m/%d) "
                 "for example(2022/01/14)"
                 "(today for default):\n"
                 )
    parse_date = date or datetime.today().strftime("%Y/%m/%d")

    def start_requests(self):
        """
        start_request method called automatically.
        Accepts from the user the date on which to search for news.
        Calls a request for vikka.ua + the specified date,
        the result is sent for processing to the method
        parse_date_page
         """
        if self.date_checking:
            parse_url = NewsDbSpider.start_urls[0] + self.parse_date
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
        next_page = response.css('.next::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse_date_page)
        for links in container:
            link = links.css('a::attr(href)').get()
            yield response.follow(link, callback=self.parse_page_info)

    def parse_page_info(self, page_response):
        """
        The method processes links to news. Extracts the necessary data
        and writes them to a csv file with a name corresponding to the
        date on which the news is selected
        """
        item = VikkaPipelineDbItem()
        tag_list = ""
        news_info = ""
        all_tags = page_response.css('a.post-tag::text').getall()
        all_text = page_response.css('div.entry-content > p::text').getall()
        if all_tags:
            for tag in all_tags:
                tag_list += f"#{tag} "
        elif not all_tags:
            tag_list += "No tags"
        if all_text:
            for text in all_text:
                news_info += text.replace(u'\xa0', ' ')
        elif not all_text:
            news_info += "No text"
        item['title_name'] = page_response.css('h1.post-title::text').get()
        item['news_text'] = news_info
        item['tags'] = tag_list
        item['news_page_url'] = page_response.url
        item['date'] = page_response.css('.post-info-style::text').get()
        yield item

    def date_checking(self):
        """ date_checking method """
        date_news = self.parse_date
        time_now = datetime.today()
        date = datetime.strptime(date_news, "%Y/%m/%d")
        if date <= time_now and len(date_news) == 10:
            return True
        else:
            return False
    # 2022/01/14
    # 2022.01.14
    # 2017/11/30
    # 2017/10/30
