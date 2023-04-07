from datetime import date

def get_date_range(date1, date2):
    if date1 > date2:
        return []
    else:
        day1 = date1.toordinal()
        day2 = date2.toordinal()
        return [date.fromordinal(day) for day in range(day1, day2 + 1)]
