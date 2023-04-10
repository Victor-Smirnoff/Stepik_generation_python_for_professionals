import json
import csv
from datetime import datetime


with open('exam_results.csv', 'r', encoding='UTF-8') as file:
    content = [line.strip().split(',') for line in file.readlines()]

keys_for_dict = content[0]
content = content[1:]

for i in range(len(content)):
    for j in range(len(content[i])):
        if j == 2:
            content[i][j] = int(content[i][j])
        elif j == 3:
            content[i][j] = datetime.strptime(content[i][j], '%Y-%m-%d %H:%M:%S')

content = sorted(content, key=lambda x: (x[4], x[2], x[3]), reverse=True)

lst = []
addet_emails = []
for i in range(len(content)):
    d = {}
    for j in range(len(content[i])):
        if keys_for_dict[j] != 'score':
            d[keys_for_dict[j]] = content[i][j]
        else:
            d['best_score'] = content[i][j]

    if d['email'] not in addet_emails:
        addet_emails.append(d['email'])
        lst.append(d)

lst = lst[::-1]

for dik in lst:
    dik['date_and_time'] = datetime.strftime(dik['date_and_time'],'%Y-%m-%d %H:%M:%S')

with open('best_scores.json', 'w', encoding='UTF-8') as output_file:
    json.dump(lst, output_file, indent=3)
