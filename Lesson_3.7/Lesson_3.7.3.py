from datetime import datetime
import calendar

names = list(calendar.day_name)

today = datetime.strptime(input(), '%Y-%m-%d')

print(names[calendar.weekday(today.year, today.month, today.day)])
