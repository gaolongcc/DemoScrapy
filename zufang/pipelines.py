# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3

class ZufangPipeline(object):
    def open_spider(self, spider):
        self.con = sqlite3.connect("zufang.sqlite")
        self.cu = self.con.cursor()

    def spider_close(self, spider):
        self.con.close()

    def process_item(self, item, spider):
        print(spider.name)
        #表中有数据则删除数据
        delete_sql = "DELETE FROM zufang WHERE money > 0"
        #self.cu.execute(delete_sql)
        #self.con.commit()
        #insert_sql = "insert into zufang (title, money) values('{}','{}')".format(item['title'], item['money'])
        insert_sql = "insert into zufang (money, title) values('{}','{}')".format(item['money'], item['title'])
        self.cu.execute(insert_sql)
        self.con.commit()
        return item
