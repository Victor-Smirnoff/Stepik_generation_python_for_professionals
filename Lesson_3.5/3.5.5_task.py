from datetime import date, time, datetime, timedelta

d = {}

for _ in range(int(input())):
    first_name, last_name, date = input().split()
    d[first_name + ' ' + last_name] = datetime.strptime(date, '%d.%m.%Y')

res = []

for key, value in d.items():
    if value == min(d.values()):
        tmp = str(value.strftime('%d.%m.%Y')) + ' ' + str(key)
        res.append(tmp)

if len(res) == 1:
    print(*res)
if len(res) > 1:
    dd = res[0].split()
    print(dd[0] + ' ' + str(len(res)))
