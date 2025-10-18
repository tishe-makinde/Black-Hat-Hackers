import scrapy
from scrapy.crawler import CrawlerProcess
import json

class ExampleSpider(scrapy.Spider):
    name = "example"
    start_urls = ['https://quotes.toscrape.com']
    scraped_data = []

    def parse(self, response):
        for quote in response.css('div.quote'):
            item = {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get()
            }
            self.scraped_data.append(item)

# Create the process
process = CrawlerProcess()

# Pass the spider class, NOT an instance
process.crawl(ExampleSpider)
process.start()  # blocks until crawling finishes

# Convert scraped data to JSON
json_data = json.dumps(ExampleSpider.scraped_data, indent=2)
print(json_data)
