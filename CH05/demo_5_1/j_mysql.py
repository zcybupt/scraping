import pymysql

data = {
    'id': '20120001',
    'name': 'Bob',
    'age': 23
}

db = pymysql.connect(host='10.201.18.139', user='zcy', password='000000', db='scraping')
cursor = db.cursor()

sql = 'SELECT * FROM students WHERE age >= 20'

try:
    cursor.execute(sql)
    print('Count', cursor.rowcount) # rowcount 属性获取查询结果的条数
    # one = cursor.fetchone()
    # print('One:', one)
    # two = cursor.fetchone()
    # print('Two:', two)
    # results = cursor.fetchall()
    # print('Results:', results)
    # print('Results Type:', type(results))
    # for row in results:
    #     print(row)
    row = cursor.fetchone()
    while row:
        print('Row:', row)
        row = cursor.fetchone()
except:
    print('error')
