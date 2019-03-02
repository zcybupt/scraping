import pymongo

# client = pymongo.MongoClient(host='10.128.240.90', port=27017)
client = pymongo.MongoClient('mongodb://10.128.240.90:27017')

# 指定数据库
# db = client.test
db = client['test']

# 指定集合
# collection = db.students
collection = db['students']

print(client)
