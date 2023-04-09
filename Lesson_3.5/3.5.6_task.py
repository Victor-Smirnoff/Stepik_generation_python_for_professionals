from datetime import date, time, datetime, timedelta

d = {}

for _ in range(int(input())):
    first_name, last_name, data = input().split()
    if data not in d.keys():
        d[data] = 1
    else:
        d[data] += 1

res = []

for key, value in d.items():
    if d[key] == max(d.values()):
        res.append(key)

res2 = []

if len(res) == 1:
    print(*res)
elif len(res) > 1:
    for dt in res:
        res2.append(datetime.strptime(dt, '%d.%m.%Y'))
    res2 = sorted(res2)
    res3 = []
    for x in res2:
        res3.append(x.strftime('%d.%m.%Y'))

    print(*res3, sep='\n')
