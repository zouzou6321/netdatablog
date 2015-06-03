# -*- coding: utf-8 -*-

# Scrapy settings for newsspider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'newsspider'

SPIDER_MODULES = ['newsspider.spiders']
NEWSPIDER_MODULE = 'newsspider.spiders'
DOWNLOAD_DELAY = 5
ITEM_PIPELINES = {'newsspider.pipelines.NewsspiderPipeline': 1
                  }
CONCURRENT_REQUESTS = 1
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'newsspider (+http://www.yourdomain.com)'
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64; rv:7.0.1) Gecko/20100101 Firefox/7.7'
DOWNLOAD_TIMEOUT = 15