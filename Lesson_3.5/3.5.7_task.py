from datetime import date, time, datetime, timedelta

today_date = datetime.strptime(input(), '%d.%m.%Y')
data_start = today_date + timedelta(days=1)
data_end = data_start + timedelta(days=7)

lst_of_dates = [(date.fromordinal(dt).day, date.fromordinal(dt).month) for dt in range(data_start.toordinal(), data_end.toordinal())]

d = {}

for _ in range(int(input())):
    first_name, last_name, data = input().split()
    data2 = datetime.strptime(data, '%d.%m.%Y')
    if (data2.day, data2.month) in lst_of_dates:
        d[first_name + ' ' + last_name] = data2

if len(d) == 0:
    print('Дни рождения не планируются')
else:
    for key, value in d.items():
        if d[key] == max(d.values()):
            print(key)
