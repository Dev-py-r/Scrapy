# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# import sqlite3
# import pymongo

class QuotetutorialPipeline:


    # def process_item(self, item, spider):
    #     print("Pipeline :" + item['title'][0])
    #     return item
    # classes and object

    # def __init__(self):
    #     self.create_connection()
    #     self.create_table()
    #
    # def create_connection(self):
    #     self.conn = sqlite3.connect("myquotes1.db")
    #     self.curr = self.conn.cursor()
    #
    # def create_table(self):
    #     self.curr.execute("""DROP TABLE IF EXISTS quotes_tb1""")
    #     self.curr.execute("""create table quotes_tb1(
    #                                 title text,
    #                                 author text,
    #                                 tag text
    #                                 )""")
    #
    # def process_item(self, item, spider):
    #     self.store_db(item)
    #     # print("Pipeline :" + item['title'][0])
    #     return item
    #
    #
    #
    # def store_db(self, item):
    #     self.curr.execute("""insert into quotes_tb1 values(?, ?, ?)""",(
    #         item['title'][0],
    #         item['author'][0],
    #         item['tag'][0]
    #
    #     ))
    #
    #     self.conn.commit()

    # def __init__(self):
    #     self.conn = pymongo.MongoClient(
    #         'localhost',
    #         27017
    #     )
    #
    #     db = self.conn['myquotes']
    #     self.collection = db['quotes_tb']
    #
    # def process_item(self, item, spider):
    #     self.collection.insert(dict(item))
    #     return item

    #Scraping through different pages
        def process_item(self, item, spider):
         return item
