# -*- coding: utf-8 -*-
import scrapy


class ApythonSpider(scrapy.Spider):
    name = 'apython'
    allowed_domains = ['http://pythonworkshops.com/#workshops']
    start_urls = ['http://pythonworkshops.com/#workshops']

    def parse(self, response):
        
        sections = response.css("section")
        #print(response.body)
        for sec in response.css("a[href='#']").extract():
            #print("*************************")
            #print("\n",sec.css("section::text"))
            print("--------->",sec)
            #print("*************************")