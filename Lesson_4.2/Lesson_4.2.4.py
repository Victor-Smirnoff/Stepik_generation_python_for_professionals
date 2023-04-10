import csv

with open('salary_data.csv', 'r', encoding='utf-8') as my_file:
    rows = csv.reader(my_file, delimiter=';')
    content = [row for row in rows]

del content[0]

d = {}
for i in range(len(content)):
    if content[i][0] not in d.keys():
        d[content[i][0]] = []
        d[content[i][0]].append(int(content[i][1]))
    else:
        d[content[i][0]].append(int(content[i][1]))

d2 = {}
for key in sorted(d.keys()):
    if key not in d2.keys():
        d2[key] = sum(d[key]) / len(d[key])

d2_val = sorted(d2.values())
for x in d2_val:
    for key, value in d2.items():
        if x == value:
            print(key)
