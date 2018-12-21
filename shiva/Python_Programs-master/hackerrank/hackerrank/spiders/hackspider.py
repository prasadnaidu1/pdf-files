# -*- coding: utf-8 -*-
import scrapy


class HackspiderSpider(scrapy.Spider):
    name = 'hackspider'
    allowed_domains = ['https://www.hackerrank.com/sivagembali?hr_r=1']
    start_urls = ['https://www.hackerrank.com/sivagembali?hr_r=1']

    def parse(self, response):
        print("Data:",response.body)
