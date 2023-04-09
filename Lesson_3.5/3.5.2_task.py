from datetime import date, time, datetime, timedelta

start_day = datetime.strptime('01.01.0001', '%d.%m.%Y').toordinal()
end_day = datetime.strptime('31.12.9999', '%d.%m.%Y').toordinal()

d = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, }

for day in range(start_day, end_day + 1):
    if date.fromordinal(day).day == 13:
        d[str(date.fromordinal(day).weekday())] += 1

for key in d:
    print(d[key])
