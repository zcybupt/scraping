import pymysql

data = {
    'id': '20120001',
    'name': 'Bob',
    'age': 21
}

db = pymysql.connect(host='10.201.18.139', user='zcy', password='000000', db='scraping')
cursor = db.cursor()

table = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))

sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)

try:
    if cursor.execute(sql, tuple(data.values())):
        print('Successful')
        db.commit()
except:
    print('Failed')
    db.rollback()
db.close()
