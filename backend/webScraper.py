import scrapy
from scrapy.crawler import CrawlerProcess
from twisted.internet import defer


class ArticleSpider(scrapy.Spider):
    name = "article_spider"

    def __init__(self, url=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = [url] if url else []

    def parse(self, response):
        yield {
            "title": response.css("h1::text").get(),
            "author": response.css("span.author::text").get(),
            "description": response.css("meta[name='description']::attr(content)").get(),
        }


class WebScraper:
    def __init__(self):
        self.results = []

    def scrape(self, url):
        """
        Scrapes a single URL and returns a dictionary with title, author, description.
        """
        process = CrawlerProcess(settings={
            "LOG_LEVEL": "ERROR",  
        })
        
        deferred = defer.Deferred()

        def crawler_results(item):
            self.results.append(item)
            deferred.callback(item)

       
        spider = ArticleSpider(url=url)
        spider.parse = lambda response: crawler_results({
            "title": response.css("h1::text").get(),
            "author": response.css("span.author::text").get(),
            "description": response.css("meta[name='description']::attr(content)").get(),
        })

        process.crawl(spider)
        process.start()  
