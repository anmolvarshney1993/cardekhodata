# -*- coding: utf-8 -*-

# Scrapy settings for imgur project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'imgur'

SPIDER_MODULES = ['imgur.spiders']
NEWSPIDER_MODULE = 'imgur.spiders'
ITEM_PIPELINES = {'scrapy.pipelines.images.ImagesPipeline': 1}
IMAGES_STORE = '/home/anmol/Documents/downimages'


# IMAGES_THUMBS = {
#     'small': (50, 50),
#     'big': (270, 270),
# }


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'imgur (+http://www.yourdomain.com)'
