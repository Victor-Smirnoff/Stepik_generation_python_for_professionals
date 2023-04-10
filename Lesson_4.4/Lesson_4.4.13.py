import json
from datetime import datetime


time1 = datetime.strptime('10:00', '%H:%M')
time2 = datetime.strptime('12:00', '%H:%M')

with open('pools.json', 'r', encoding='utf-8') as file:
    content = json.load(file)

res = []
for pool in content:
    flag = 0
    for day in pool["WorkingHoursSummer"]:
        t1 = datetime.strptime(pool["WorkingHoursSummer"][day].split('-')[0], '%H:%M')
        t2 = datetime.strptime(pool["WorkingHoursSummer"][day].split('-')[1], '%H:%M')
        if t1 <= time1 and t2 >= time2:
            flag += 1
    if flag == 7:
        res.append(pool)

def key_to_sort(d):
    return d["DimensionsSummer"]["Length"], d["DimensionsSummer"]["Width"]

res = sorted(res, key=key_to_sort, reverse=True)

print(str(res[0]['DimensionsSummer']['Length']) + 'x' + str(res[0]['DimensionsSummer']['Width']))
print(res[0]['Address'])
