from datetime import date, datetime


def get_booking_list(lst_with_dates):
    res_lst = []
    if type(lst_with_dates) == list:
        for book_date in lst_with_dates:
            if '-' not in book_date:
                my_date = datetime.strptime(book_date, '%d.%m.%Y').toordinal()
                res_lst.append(my_date)
            else:
                book_date = book_date.split('-')
                tmp = []
                for dt in book_date:
                    my_date = datetime.strptime(dt, '%d.%m.%Y').toordinal()
                    tmp.append(my_date)
                for day in range(tmp[0], tmp[1] + 1):
                    res_lst.append(day)

    if type(lst_with_dates) == str:
        if '-' not in lst_with_dates:
            my_date = datetime.strptime(lst_with_dates, '%d.%m.%Y').toordinal()
            res_lst.append(my_date)
        else:
            book_date = lst_with_dates.split('-')
            tmp = []
            for dt in book_date:
                my_date = datetime.strptime(dt, '%d.%m.%Y').toordinal()
                tmp.append(my_date)
            for day in range(tmp[0], tmp[1] + 1):
                res_lst.append(day)

    return res_lst


def is_available_date(booked_dates, date_for_booking):
    booked_lst = set(get_booking_list(booked_dates))
    list_for_booking = set(get_booking_list(date_for_booking))
    myset = booked_lst & list_for_booking
    return True if len(myset) == 0 else False
