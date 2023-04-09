from datetime import date, datetime, timedelta, time

print((datetime.strptime(input(), '%H:%M:%S') - datetime.strptime('00:00:00', '%H:%M:%S')).seconds)




