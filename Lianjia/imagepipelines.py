#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : imagepipelines.py
# @Author: lch
# @Date  : 2018/5/31
# @Desc  :
import scrapy
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem
import os,logging

class MyImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(url=image_url, headers={'Referer': item['header_referer'],
                                                         'Agent': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'},
                                 meta={'item':item})




    def item_completed(self, results, item, info):
        images = [x['path'] for ok, x in results if ok]
        if not images:
            raise DropItem("Item contains no images")
        item['images'] = images
        return item

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        image_dir_name = r"/tmp/images/" + item['region'] + '/' + item['plot']
        if not os.path.exists(image_dir_name):
            try:
                os.makedirs(name=image_dir_name, mode=0o777)
                logging.debug('[SUCC] 创建%s目录成功！' % image_dir_name )
            except Exception as e:
                logging.debug('创建%s目录失败! [异常原因]:%s' % (image_dir_name, e))
        else:
            pass

        image_name = r"%s/%s/%s.jpg" % (item['region'], item['plot'], request.url.replace('/',''))
        return image_name
