import scrapy
import requests

class GITSpider (scrapy.Spider):
    name="your site"
    start_urls = [ "", ]

    def parse(self, response):
        
        text_value = response.css('span[data-ds-component="DS-Text"]::text').get()
        if text_value:
            self.log(f'Extracted text: {text_value}')
        else:
            self.log('No text found')