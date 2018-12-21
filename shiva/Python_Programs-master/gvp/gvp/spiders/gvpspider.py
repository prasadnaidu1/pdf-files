# -*- coding: utf-8 -*-
import scrapy


class GvpspiderSpider(scrapy.Spider):
    name = 'gvpspider'
    allowed_domains = ['https://en.wikipedia.org/wiki/Gayatri_Vidya_Parishad_College_of_Engineering']
    start_urls = ['https://en.wikipedia.org/wiki/Gayatri_Vidya_Parishad_College_of_Engineering']

    def parse(self, response):
        print("GVP Data:",response.body)
