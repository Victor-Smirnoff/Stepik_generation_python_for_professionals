from datetime import date, datetime, timedelta

dates = [(datetime.strptime(date, '%d.%m.%Y')).toordinal() for date in input().split()]

print([abs(dates[i] - dates[i + 1]) for i in range(len(dates) - 1)])
