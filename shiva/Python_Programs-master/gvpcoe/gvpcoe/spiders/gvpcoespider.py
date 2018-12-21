# -*- coding: utf-8 -*-
import scrapy
li = []

class GvpcoespiderSpider(scrapy.Spider):
    name = 'gvpcoespider'
    allowed_domains = ['http://gvpce.ac.in/result.html']
    start_urls = ['http://gvpce.ac.in/result.html']

    def parse(self, response):
        #print("------------------------------------------------------------")
        #print("Result:",response.body)
        #print("Response: ",response.css("body").extract())
        print("------------------------------------------------------------")
        #url = start_urls[0]
        for res in response.css("div.info a::attr(href)").extract():
            li.append(res)
            print("------>",res)   
        print("Length: ",len(li))
        if(len(li) > 592):
            print("Results announced")