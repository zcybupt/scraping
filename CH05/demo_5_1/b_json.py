import json

# json 中必须使用双引号
str = '''
[{
    "name": "Bob",
    "gender": "male",
    "birthday": "1992-10-18"
}, {
    "name": "Selina",
    "gender": "female",
    "birthday": "1995-10-18"
}]
'''

print(type(str))
data = json.loads(str)
print(data[0]['name'])
print(data[0]['gender'])
print(data[1]['name'])
