import mysql.connector


class insert():
    conn = ""
    cursor = ""

    def __init__(self):
        self.conn = mysql.connector.connect(user='lijinjiong', password='li841327232', database='family', host="59.110.220.27")
        self.cursor = self.conn.cursor()

    def insert(self):
        pass



# conn = mysql.connector.connect(user='lijinjiong', password='li841327232', database='family', host="59.110.220.27")
# cursor = conn.cursor()
# sql = 'insert into food (name, alias, calorie, detail_url) values (%s, %s, %s, %s)'
# cursor.execute(sql, [item["name"], item["alias"], item["calorie"], item["detail_url"]])
# conn.commit()
# cursor.close()
