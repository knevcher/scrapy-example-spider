# -*- coding: utf-8 -*-
import scrapy
import logging

from livej.items import LivejItem


class LivejSpider(scrapy.Spider):
    name = 'livej'
    start_urls = ['http://adski-kafeteri.livejournal.com/']

    def parse(self, response):
        try:
            item_urls = response.xpath('//*[@id="content"]/div/div/h3/span/a/@href').extract()
        except:
            print "!!!! NO URLS FOUND !!!!"

        for url in item_urls:
            yield scrapy.Request(url, callback=self.parse_item_page)

        next_url = response.xpath('//a[text()="Previous 10 Entries"]').xpath('@href').extract()
        if next_url:
            yield scrapy.Request(next_url[0], callback=self.parse)
        else:
            self.logger.info('No next url on page!!! %s', response.url)
            print "NO NEXT URL ON PAGE!!!!!!!!!!!!!!!!!!"

    def parse_item_page(self, response):
        item = LivejItem()
        item['title'] = response.xpath('//title/text()').extract()[0]
        item['content'] = response.xpath('//*[@id="content"]/div[1]').extract()[0]
        item['link'] = response.url
        item['image_paths'] = response.xpath('//p/img/@src').extract()

        yield item
