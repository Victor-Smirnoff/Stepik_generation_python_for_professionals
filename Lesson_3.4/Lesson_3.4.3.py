from datetime import date, datetime, timedelta

today = datetime.strptime(input(), '%d.%m.%Y')

print((today - timedelta(days=1)).strftime('%d.%m.%Y'), (today + timedelta(days=1)).strftime('%d.%m.%Y'), sep='\n')
