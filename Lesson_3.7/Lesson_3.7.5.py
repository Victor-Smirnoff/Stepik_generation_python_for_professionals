import calendar

year_today, month_today = input().split()
year_today = int(year_today)

english_names = list(calendar.month_name)

for i in range(len(english_names)):
    if month_today == english_names[i]:
        month_today = i

print(calendar.monthrange(year_today, month_today)[1])
