import pymysql

data = {
    'id': '20120001',
    'name': 'Bob',
    'age': 23
}

db = pymysql.connect(host='10.201.18.139', user='zcy', password='000000', db='scraping')
cursor = db.cursor()

table = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))

sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys,
                                                                                     values=values)
update = ','.join([" {key} = %s".format(key=key) for key in data])
sql += update
try:
    if cursor.execute(sql, tuple(data.values()) * 2):
        print(sql, tuple(data.values()) * 2)
        print('Successful')
        db.commit()
except:
    print('Failed')
    db.rollback()
db.close()
