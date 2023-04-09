import calendar

year_today, month_today = map(int, input().split())
print(calendar.monthrange(year_today, month_today)[1])




