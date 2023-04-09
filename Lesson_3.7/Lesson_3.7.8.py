import calendar
from datetime import datetime, date


def get_all_mondays(year):
    stat_date = datetime(year, 1, 1)
    monday = list(calendar.day_name).index('Thursday')
    first_monday = 0
    for i in range(stat_date.toordinal(), stat_date.toordinal() + 7):
        x = date.fromordinal(i)
        if calendar.weekday(x.year, x.month, x.day) == monday:
            first_monday = x
            break

    end_date = datetime(year, 12, 31)
    end_monday = 0
    for i in range(end_date.toordinal() - 6, end_date.toordinal() + 1):
        y = date.fromordinal(i)
        if calendar.weekday(y.year, y.month, y.day) == monday:
            end_monday = y
            break

    return [date.fromordinal(i) for i in range(first_monday.toordinal(), end_monday.toordinal() + 1, 7)]


all_thursdays = get_all_mondays(int(input()))

res = []

for m in range(1, 13):
    count = 0
    for i in range(len(all_thursdays)):
        if all_thursdays[i].month == m:
            count += 1
        if count == 3:
            res.append(all_thursdays[i].strftime('%d.%m.%Y'))
            break

print(*res, sep='\n')
