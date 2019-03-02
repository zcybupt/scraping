import pymysql

db = pymysql.connect(host='10.201.18.139', user='zcy', password='000000', port=3306, db='scraping')
cursor = db.cursor()  # 获得 MySQL 操作游标, 利用游标来执行 SQL 语句
sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR (255) NOT NULL, name VARCHAR (255) NOT NULL, age INT NOT ' \
      'NULL, PRIMARY KEY (id))'
# cursor.execute('SELECT VERSION()')
# data = cursor.fetchone()
# print('Database version: ', data)
# cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")
cursor.execute(sql)
db.close()
