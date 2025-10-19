import scrapy
from scrapy.crawler import CrawlerProcess
import json
import multiprocessing

class ExampleSpider(scrapy.Spider):
    name = "example"
    custom_settings = {
        "LOG_LEVEL": "ERROR",
        "RETRY_ENABLED": True,
        "RETRY_TIMES": 2,
        "DOWNLOAD_TIMEOUT": 5,
        "CONCURRENT_REQUESTS": 2,
    }

    def __init__(self, url=None, collector=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = [url] if url else []
        self.collector = collector

    def parse(self, response):
        description = response.css('meta[name="description"]::attr(content)').get()
        title = response.css('title::text').get()
        paragraphs = response.css('p::text').getall()

        item = {"description": description, "title": title, "paragraphs": paragraphs}
        self.collector.append(item)

class webScraper:
    def __init__(self, link):
        self.link = link

    def _run_spider(self, collector):
        process = CrawlerProcess(settings={"LOG_LEVEL": "ERROR"})
        process.crawl(ExampleSpider, url=self.link, collector=collector)
        process.start()

    def scrape(self):
        manager = multiprocessing.Manager()
        collector = manager.list()

        process = multiprocessing.Process(target=self._run_spider, args=(collector,))
        process.start()
        process.join()

        return json.dumps(list(collector), indent=2)
