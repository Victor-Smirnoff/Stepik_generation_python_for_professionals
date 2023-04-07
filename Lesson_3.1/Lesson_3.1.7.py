from datetime import date

def  saturdays_between_two_dates(date1, date2):
    day1 = date1.toordinal()
    day2 = date2.toordinal()
    count = 0
    if day1 <= day2:
        for day in range(day1, day2 + 1):
            if date.fromordinal(day).weekday() == 5:
                count += 1
    if day1 > day2:
        for day in range(day2, day1 + 1):
            if date.fromordinal(day).weekday() == 5:
                count += 1
    return count
