# -*- coding: utf-8 -*-
import scrapy


class AttendenceSpider(scrapy.Spider):
    name = 'attendence'
    allowed_domains = ['http://pythonworkshops.com']
    start_urls = ['http://pythonworkshops.com']

    def parse(self, response):
        print("*****************************************")
        print(response.body)
        #print("Result:",response.css("body").extract())
        print("*****************************************")
