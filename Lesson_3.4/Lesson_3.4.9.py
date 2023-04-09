from datetime import date, datetime, timedelta

def fill_up_missing_dates(dates):
    dates = [(datetime.strptime(dt, '%d.%m.%Y')).toordinal() for dt in dates]
    return [date.fromordinal(dt).strftime('%d.%m.%Y') for dt in range(min(dates), max(dates) + 1)]
