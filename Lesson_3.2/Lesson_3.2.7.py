from datetime import date

def print_good_dates(dates):
    res = []
    for d in dates:
        if d.year == 1992 and d.month + d.day == 29:
            res.append(d)
    res = sorted(res)
    for x in res:
        print(x.strftime('%B %d, %Y'))
