from datetime import date

date1, date2 = date.fromisoformat(input()), date.fromisoformat(input())

if date1 > date2:
    date1, date2 = date2, date1

print(date1.strftime('%d-%m (%Y)'))
