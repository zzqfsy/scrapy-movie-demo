# -*- coding: utf-8 -*-
import scrapy
from movie.items import MovieItem


class MeijuSpider(scrapy.Spider):
    name = 'meiju'
    allowed_domains = ['meijutt.com']
    start_urls = ['http://www.meijutt.com/new100.html']

    def parse(self, response):
        movies = response.xpath('//ul[@class="top-list  fn-clear"]/li')
        for each_movie in movies:
            item = MovieItem()
            item['name'] = each_movie.xpath('./h5/a/@title').extract()[0]

            state = each_movie.xpath('./span[@class="state1 new100state1"]/font/text()').extract();
            if state:
                item['state'] = state[0]
            else:
                item['state'] = each_movie.xpath('./span[@class="state1 new100state1"]/text()').extract()[0]

            item['type'] = each_movie.xpath('./span[@class="mjjq"]/text()').extract()[0]

            updateDate = each_movie.xpath('./div/font/text()').extract()
            if updateDate:
                item['updateDate'] = updateDate[0]
            else:
                item['updateDate'] = each_movie.xpath('./div/text()').extract()[0]

            yield item
