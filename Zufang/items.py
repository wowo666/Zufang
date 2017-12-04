# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
'''house_title
link
price
method付款方式
lease租赁方式
type房屋类型
floor楼层
estate小区
addr地址
tel电话
decoration装修
desc描述

'''

class ZufangItem(scrapy.Item):
    # define the fields for your item here like:
    house_title = scrapy.Field()
    link = scrapy.Field()
    price = scrapy.Field()
    lease = scrapy.Field()
    type = scrapy.Field()
    floor = scrapy.Field()
    estate = scrapy.Field()
    addr = scrapy.Field()
    tel = scrapy.Field()
    decoration = scrapy.Field()
    desc = scrapy.Field()
    area = scrapy.Field()
    configuration = scrapy.Field()
    pubdate = scrapy.Field()
    number = scrapy.Field()
    source = scrapy.Field()