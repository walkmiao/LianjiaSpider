# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    #价格
    price = scrapy.Field()
    #面积
    area = scrapy.Field()
    #房屋户型
    home_type = scrapy.Field()
    #房屋楼层
    home_floor = scrapy.Field()
    #房屋朝向
    home_towards = scrapy.Field()
    #地铁信息
    metro = scrapy.Field()
    #小区名称
    plot = scrapy.Field()
    #小区所属区
    region = scrapy.Field()
    #小区具体位置
    location = scrapy.Field()
    #发布时间
    release_time = scrapy.Field()
    #联系人
    contact_people = scrapy.Field()
    #联系电话
    phone = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    header_referer = scrapy.Field()
