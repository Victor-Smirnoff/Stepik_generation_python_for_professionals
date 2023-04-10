import csv
from datetime import datetime

with open('name_log.csv', 'r', encoding='utf-8') as my_file:
    rows = csv.reader(my_file, delimiter=',')
    content = [row for row in rows]

first_line = ','.join(content.pop(0))

content = [[content[i][0], content[i][1], datetime.strptime(content[i][2], '%d/%m/%Y %H:%M')] for i in range(len(content))]

d = {}

for i in range(len(content)):
    if content[i][1] not in d.keys():
        d[content[i][1]] = []
        d[content[i][1]].append(content[i])
    else:
        d[content[i][1]].append(content[i])

res = []
for key, value in d.items():
    if len(d[key]) == 1:
        res.append(value)

res2 = []
for i in range(len(res)):
    res2.append(res[i][0])

for key, value in d.items():
    if len(d[key]) != 1:
        value = sorted(value, key=lambda x: x[2])
        res2.append(value[-1])

for i in range(len(res2)):
    res2[i][2] = res2[i][2].strftime('%d/%m/%Y %H:%M')

res2 = [x[0] + ',' + x[1] + ',' + x[2] for x in sorted(res2, key=lambda x: x[1])]

with open('new_name_log.csv', 'w', encoding='utf-8') as output_file:
    print(first_line, file=output_file)
    for x in res2:
        print(x, file=output_file)
