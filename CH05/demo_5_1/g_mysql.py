import pymysql

data = {
    'id': '2016213431',
    'name': 'Bob',
    'age': 20
}

db = pymysql.connect(host='10.201.18.139', user='zcy', password='000000', db='scraping')
cursor = db.cursor()
table = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))
sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
print(sql)
print(['%s'] * len(data))
try:
    if cursor.execute(sql, tuple(data.values())):
        print('Successful')
        db.commit()
except:
    print('Failed')
    db.rollback()
db.close()
