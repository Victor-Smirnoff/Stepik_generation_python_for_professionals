from datetime import date, time, datetime, timedelta

start_date = datetime.strptime(input(), '%d.%m.%Y')
end_date = datetime.strptime(input(), '%d.%m.%Y')

res = []
for dt in range(start_date.toordinal(), end_date.toordinal() + 1):
    da = date.fromordinal(dt)
    if (da.day + da.month) % 2 != 0:
        res.append(da)
        break
    else:
        continue

for ddt in range(res[0].toordinal() + 3, end_date.toordinal() + 1, 3):
    dat = date.fromordinal(ddt)
    if dat.weekday() != 0 and dat.weekday() != 3:
        res.append(dat)

res = [my_date.strftime('%d.%m.%Y') for my_date in res if (my_date.weekday() != 0 and my_date.weekday() != 3)]

print(*res, sep='\n')
