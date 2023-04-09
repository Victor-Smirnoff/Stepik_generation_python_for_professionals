from datetime import date, datetime, timedelta

def num_of_sundays(year):
    first_date = date(year, 1, 1)
    second_date = date(year, 12, 31)
    count_sundays = 0
    for day in range(first_date.toordinal(), second_date.toordinal() + 1):
        if date.fromordinal(day).weekday() == 6:
            count_sundays += 1
    return count_sundays
