# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb,os,sys
reload(sys)
sys.setdefaultencoding('utf8')
if 'SERVER_SOFTWARE' in os.environ:
    MYSQL_HOST = 'rdsrayzenzjnv7v.mysql.rds.aliyuncs.com'
    MYSQL_PORT = 3306
    MYSQL_USER = 'chongwug'
    MYSQL_PASS = 'weet6321'
    MYSQL_DB = 'datablog'
else:
    # Make `python manage.py syncdb` works happy!
    MYSQL_HOST = 'localhost'
    MYSQL_PORT = 3306
    MYSQL_USER = 'root'
    MYSQL_PASS = 'root'
    MYSQL_DB = 'datablog'

MYSQL_HOST = 'rdsrayzenzjnv7v.mysql.rds.aliyuncs.com'
MYSQL_PORT = 3306
MYSQL_USER = 'chongwug'
MYSQL_PASS = 'weet6321'
MYSQL_DB = 'datablog'

class NewsspiderPipeline(object):
    def process_item(self, item, spider):
        if spider.name != "news":
            return item
        if item.get("news_thread", None) is None:
            return item
        conn = MySQLdb.connect(host=MYSQL_HOST,user=MYSQL_USER,passwd=MYSQL_PASS,db=MYSQL_DB,port=MYSQL_PORT)
        conn.set_character_set('utf8')
        cur = conn.cursor()
        sql = u"select * from blog_news where news_thread='%s'" % item['news_thread']
        cur.execute(sql)
        has_data = False
        for row in cur:
            has_data = True
        if has_data:
            return
        else:
            sql = u"insert into `blog_news`(`news_thread`, `news_title`,`news_url`, `news_time`, `news_from`, `from_url`, `news_body`) \
            VALUES ('%s','%s','%s','%s','%s','%s','%s')" % (
                item['news_thread'].encode('utf-8'),
                item['news_title'].encode('utf-8'),
                item['news_url'].encode('utf-8'),
                item['news_time'].encode('utf-8'),
                item['news_from'].encode('utf-8'),
                item['from_url'].encode('utf-8'),
                item['news_body']
            )
            # print(sql)
            cur.execute(sql)
            conn.commit()
        conn.close()
