# -*- coding: utf-8 -*-

import os
from urlparse import urlparse

from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request
from scrapy.exceptions import DropItem

from livej import settings


class LivejPipeline(object):

    def __init__(self):
        if not os.path.isdir(settings.STORAGE_PATH):
            os.mkdir(settings.STORAGE_PATH)
        elif not os.access(settings.STORAGE_PATH, os.W_OK):
            raise Exception('Can\' write dir!!!')

    def process_item(self, item, spider):
        pass


class LJImagesPipeline(ImagesPipeline):

    def file_path(self, request, response=None, info=None):
        ## start of deprecation warning block (can be removed in the future)
        def _warn():
            from scrapy.exceptions import ScrapyDeprecationWarning
            import warnings
            warnings.warn('ImagesPipeline.image_key(url) and file_key(url) methods are deprecated, '
                          'please use file_path(request, response=None, info=None) instead',
                          category=ScrapyDeprecationWarning, stacklevel=1)

        # check if called from image_key or file_key with url as first argument
        if not isinstance(request, Request):
            _warn()
            url = request
        else:
            url = request.url

        # detect if file_key() or image_key() methods have been overridden
        if not hasattr(self.file_key, '_base'):
            _warn()
            return self.file_key(url)
        elif not hasattr(self.image_key, '_base'):
            _warn()
            return self.image_key(url)
        ## end of deprecation warning block

        image_guid = request.url.split('/')[-1]
        return '%s_%s' % (request.meta['save_path'], image_guid)

    def get_media_requests(self, item, info):
        for image_url in item['image_paths']:
            yield Request(image_url, meta=dict(save_path=dir_for_item(item)))

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths

        return item


def dir_for_item(item):
    item_path = urlparse(item['link']).path
    return os.path.split(item_path)[1].replace('.html', '')
