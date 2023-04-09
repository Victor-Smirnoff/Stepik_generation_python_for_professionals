import calendar
from datetime import datetime, date


def get_days_in_month(year, month):
    english_names = list(calendar.month_name)
    for i in range(len(english_names)):
        if month == english_names[i]:
            month = i

    stat_date = datetime(year, month, 1)
    return [date.fromordinal(i) for i in range(stat_date.toordinal(), stat_date.toordinal() + calendar.monthrange(year, month)[1])]
