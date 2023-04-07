from datetime import date

def get_min_max(dates):
    if len(dates) == 0:
        return ()
    else:
        return min(dates), max(dates)
