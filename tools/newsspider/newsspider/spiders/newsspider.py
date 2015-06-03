from ..items import NewsspiderItem
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import Selector


class newsspider(CrawlSpider):
    name = "news"
    download_delay = 5
    allowed_domains = ["163.com"]
    start_urls = ['http://news.163.com/']
    rules = (
        Rule(LinkExtractor(allow=r"/15/\d+/\d+/*"),
             callback="parse_news", follow=True),
    )
    #print('###########')
    def parse_news(self, response):
        item = NewsspiderItem()
        url_token = response.url.strip().split('/')
        item['news_thread'] = url_token[-4] + url_token[-3] + url_token[-2] + url_token[-1][:-5]
        # self.get_thread(response,item)
        self.get_title(response,item)
        self.get_source(response,item)
        self.get_url(response,item)
        self.get_news_from(response,item)
        self.get_from_url(response,item)
        self.get_text(response,item)
        return item

    def get_title(self,response,item):
        title=response.xpath("/html/head/title/text()").extract()
        if title:
            # print 'title:'+title[0][:-5].encode('utf-8')
            item['news_title']=title[0][:-5]
        else:
            item['news_title']=""

    def get_source(self,response,item):
        source=response.xpath("//div[@class='ep-time-soure cDGray']/text()").extract()
        if source:
            # print 'source'+source[0][:-5].encode('utf-8')
            item['news_time']=source[0][:-5]
        else:
            item['news_time']=""

    def get_news_from(self,response,item):
        news_from=response.xpath("//a[@id='ne_article_source']/text()").extract()
        if news_from:
            # print 'from'+news_from[0].encode('utf-8')
            item['news_from']=news_from[0]
        else:
            item['news_from']=""

    def get_from_url(self,response,item):
        from_url=response.xpath("//div[@class='left']/a/@href").extract()
        if from_url:
            # print 'url'+from_url[0].encode('utf-8')
            item['from_url']=from_url[0]
        else:
            item['from_url']=""

    def get_text(self,response,item):
        sel = Selector(response)
        news_body=sel.xpath("//div[@id='endText']/p").extract()
        item['news_body']=""
        for new_body in news_body:
            contentsel = Selector(text=new_body)
            localcontens = contentsel.xpath("string(//p)").extract()
            for localconten in localcontens:
                item['news_body'] += localconten

    def get_url(self, response, item):
        news_url=response.url
        if news_url:
            #print news_url
            item['news_url']=news_url
        else:
            item['news_url']=""
