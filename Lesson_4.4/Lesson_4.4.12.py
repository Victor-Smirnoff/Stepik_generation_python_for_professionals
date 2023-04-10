import json


with open('students.json', 'r', encoding='utf-8') as f:
    content = json.load(f)

res = ['name,phone'] + sorted([student['name'] + ',' + student['phone'] for student in content if student['age'] >= 18 and student['progress'] >= 75])

with open('data.csv', 'w', encoding='utf-8') as out:
    for x in res:
        print(x, file=out)
