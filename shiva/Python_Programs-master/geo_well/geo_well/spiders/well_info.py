# -*- coding: utf-8 -*-
import scrapy


class WellInfoSpider(scrapy.Spider):
    name = 'well_info'
    allowed_domains = ['http://59.144.184.77:8085/AGLService/serviceWiseEmpMappingReport']
    start_urls = ['http://59.144.184.77:8085/AGLService/serviceWiseEmpMappingReport']

    def parse(self, response):
        print("------------------------")
        print(response.body)
        print("------------------------")
