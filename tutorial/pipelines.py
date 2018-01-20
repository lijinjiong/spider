# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

# if item:
#     conn = mysql.connector.connect(user='lijinjiong', password='li841327232', database='family', host="59.110.220.27")
#     cursor = conn.cursor()
#     res = cursor.execute('insert into food_category (origin_url, name ) values (%s, %s)', [item["url"], item["name"]])
#     print("insert success %s ;", [res])
#     cursor.close()

import mysql.connector


class TutorialPipeline(object):

    def process_item(self, item, spider):
        if item:
            conn = mysql.connector.connect(user='lijinjiong', password='li841327232', database='family', host="59.110.220.27")
            cursor = conn.cursor()
            sql = 'insert into food (name, alias, calorie, detail_url) values (%s, %s, %s, %s)'
            cursor.execute(sql, [item["name"], item["alias"], item["calorie"], item["detail_url"]])
            conn.commit()
            cursor.close()
        return item
