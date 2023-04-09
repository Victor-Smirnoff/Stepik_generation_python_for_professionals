from datetime import date, datetime, timedelta

today = datetime.strptime(input(), '%d.%m.%Y')
print((date.fromordinal(today.toordinal())).strftime('%d.%m.%Y'))

start = 2
for task in range(9):
    print((date.fromordinal(today.toordinal() + start)).strftime('%d.%m.%Y'))
    today = date.fromordinal(today.toordinal() + start)
    start += 1
