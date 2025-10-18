import scrapy
from scrapy.crawler import CrawlerProcess
from twisted.internet import defer
import json
import multiprocessing

class ExampleSpider(scrapy.Spider):


    name = "example"

    def __init__(self, url=None, collector=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = [url] if url else []
        self.collector = collector  # shared list to store results

    def parse(self, response):
        description = response.css('meta[name="description"]::attr(content)').get()
        title = response.css('title::text').get()

        item = {
            "description": description,
            "title": title
        }

        self.collector.append(item)
        
        # for quote in response.css('div.quote'):
        #     item = {
        #         'text': quote.css('span.text::text').get(),
        #         'author': quote.css('small.author::text').get()
        #     }
        #     if self.collector is not None:
        #         self.collector.append(item)

class webScraper:
    def __init__(self, link):
        self.link = link
        self.results = []
    
        process = CrawlerProcess(settings={
            "LOG_LEVEL": "ERROR",
        })
        # Pass the spider class, NOT an instance
        process.crawl(ExampleSpider, url=self.link, collector=self.results)
        process.start()  # blocks until crawling finishes

        # Convert scraped data to JSON
        json_data = json.dumps(self.results, indent=2)
        self.results = json_data

    def scrape(self):
        return self.results

