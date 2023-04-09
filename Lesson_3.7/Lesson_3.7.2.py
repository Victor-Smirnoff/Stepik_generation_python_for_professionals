import calendar

input_year, input_month = input().split()
input_year = int(input_year)

for i in range(len(calendar.month_abbr)):
    if input_month == calendar.month_abbr[i]:
        input_month_number = i

calendar.prmonth(input_year, input_month_number)
