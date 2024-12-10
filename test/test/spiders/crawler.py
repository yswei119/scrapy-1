import scrapy
import pandas as pd

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    path = '/Users/yswei/Desktop/scrapy/test/a.csv'
    def start_requests(self):
        url = "https://quotes.toscrape.com/"
        tag = getattr(self, "tag", None)
        if tag is not None:
            url = url + "tag/" + tag
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        print(response.url)
        a = []
        for quote in response.css("div.quote"):
            #yield {
            #    "text": quote.css("span.text::text").get(),
            #    "author": quote.css("small.author::text").get(),
            #}
            a.append({
               "text": quote.css("span.text::text").get(),
               "author": quote.css("small.author::text").get(),
            })
        print('Data size',len(a),a)

        next_page = response.css("li.next a::attr(href)").get()
        print('='*100)
        print('Next Page:',next_page)
        print('='*100)
        if next_page is not None:
            yield response.follow(next_page, self.parse)