# -*- coding: utf-8 -*-
import scrapy
import logging
from Lianjia.items import LianjiaItem
class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['lianjia.com']
    start_urls = ["https://nj.lianjia.com/zufang/"]

    def parse(self, response):
        totalPage = eval(response.xpath('//div[@class="page-box house-lst-page-box"]/@page-data').extract()[0]).get('totalPage')
        curPage = eval(response.xpath('//div[@class="page-box house-lst-page-box"]/@page-data').extract()[0]).get('curPage')
        urls=[]
        for i in response.xpath('//ul[@id="house-lst" and @class="house-lst"]//li'):
            url=i.xpath('div[@class="pic-panel"]/a/@href').extract()[0]
            urls.append(url)
        logging.debug('当前页:{0},url总数:{1}'.format(curPage,len(urls)))

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_info)
        if curPage < 100:
            next_url=self.start_urls[0] + 'pg{}'.format(curPage+1) + '/'
            logging.debug('第{0}页爬取完毕,准备爬取{1}! 爬取进度:{2} %'.format(curPage,curPage+1,(curPage+1)/totalPage*100))
            yield scrapy.Request(url=next_url,callback=self.parse)
    def parse_info(self, response):
        item = LianjiaItem()
        try:
            item['price'] = response.xpath('//div[@class="content zf-content"]/div[@class="price "]/span[@class="total"]/text()').extract()[0]
        except:
            item['price'] = None
        try:
            item['area'] = response.xpath('//div[@class="content zf-content"]/div[@class="zf-room"]/p[1]/text()').extract()[0]
        except:
            item['area'] = None
        try:
            item['home_type'] = response.xpath('//div[@class="content zf-content"]/div[@class="zf-room"]/p[2]/text()').extract()[0]
        except:
            item['home_type'] = None
        try:
            item['home_floor'] = response.xpath('//div[@class="content zf-content"]/div[@class="zf-room"]/p[3]/text()').extract()[0]
        except:
            item['home_floor'] = None
        try:
            item['home_towards'] = response.xpath('//div[@class="content zf-content"]/div[@class="zf-room"]/p[4]/text()').extract()[0]
        except:
            item['home_towards'] = None
        try:
            item['metro'] = response.xpath('//div[@class="content zf-content"]/div[@class="zf-room"]/p[5]/text()').extract()[0]
        except:
            item['metro'] = None
        try:
            item['plot'] = response.xpath('//div[@class="content zf-content"]/div[@class="zf-room"]/p[6]/a[1]/text()').extract()[0]
        except:
            item['plot'] = None
        try:
            item['region'] = response.xpath('//div[@class="content zf-content"]/div[@class="zf-room"]/p[7]/a/text()').extract()[0]
        except:
            item['region'] = None
        try:
            item['location'] = response.xpath('//div[@class="content zf-content"]/div[@class="zf-room"]/p[7]/a/text()').extract()[1]
        except:
            item['location'] = None
        try:
            item['release_time'] = response.xpath('//div[@class="content zf-content"]/div[@class="zf-room"]/p[8]/text()').extract()[0]
        except:
            item['release_time'] = None
        try:
            item['contact_people'] = response.xpath('//div[@class="content zf-content"]//div[@class="brokerName"]/a/text()').extract()[0]
        except:
            item['contact_people'] = None
        try:
            item['phone'] = response.xpath('//div[@class="content zf-content"]//div[@class="phone"]/text()').extract()[0].replace(' ','').replace('\n','')+'转'\
                            +response.xpath('//div[@class="content zf-content"]//div[@class="phone"]/text()').extract()[1].replace(' ','').replace('\n','')
        except:
                item['phone'] = None
        try:
            item['image_urls'] = []
            for i in response.xpath('//div[@class="img"]/div[@class="thumbnail"]//li/@data-src'):
                item['image_urls'].append(i.extract())
        except:
            item['image_urls'] = None

        item['header_referer'] = response.url

        yield item
