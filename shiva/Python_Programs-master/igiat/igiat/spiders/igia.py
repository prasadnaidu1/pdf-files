# -*- coding: utf-8 -*-
import scrapy


class IgiaSpider(scrapy.Spider):
    name = 'igia'
    allowed_domains = ['http://www.igiat.com/']
    start_urls = ['http://www.igiat.com']

    def parse(self, response):
        print("Result:",response.body)
