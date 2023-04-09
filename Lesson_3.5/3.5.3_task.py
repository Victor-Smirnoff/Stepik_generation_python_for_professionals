from datetime import date, time, datetime, timedelta

today_date_time = datetime.strptime(input(), '%d.%m.%Y %H:%M')
today_date = datetime.fromordinal(today_date_time.toordinal())

if today_date_time.weekday() in [0, 1, 2, 3, 4]:
    start_work_day = today_date + timedelta(hours=9)
    end_work_day = today_date + timedelta(hours=21)
    if start_work_day <= today_date_time < end_work_day:
        print(int((end_work_day - today_date_time).seconds / 60))
    else:
        print('Магазин не работает')

if today_date_time.weekday() in [5, 6]:
    start_work_day = today_date + timedelta(hours=10)
    end_work_day = today_date + timedelta(hours=18)
    if start_work_day <= today_date_time < end_work_day:
        print(int((end_work_day - today_date_time).seconds / 60))
    else:
        print('Магазин не работает')
