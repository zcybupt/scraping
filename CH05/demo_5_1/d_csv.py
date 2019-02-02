import csv

with open('data.csv', 'w', encoding='utf-8') as csvfile:
    fieldnames = ['id', 'name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'id': '100001', 'name': 'Mike', 'age': 20})
    writer.writerow({'id': '100002', 'name': 'Bob', 'age': 22})
    writer.writerow({'id': '100003', 'name': 'Jordan', 'age': 21})

with open('data.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
