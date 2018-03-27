# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class MoviePipeline(object):
    def process_item(self, item, spider):
        # return item
        with open("meiju.txt", 'a', encoding='utf-8') as fp:
            fp.write(item['name'] + ' ' + item['state'] + ' ' + item['type'] + ' ' + item['updateDate'] +'\n')