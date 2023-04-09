from datetime import date, datetime, timedelta

start_task = datetime.strptime(input(), '%H:%M')
end_task = datetime.strptime(input(), '%H:%M')

while end_task >= start_task + timedelta(minutes=45):
    print(f'{start_task.strftime("%H:%M")} - {(start_task + timedelta(minutes=45)).strftime("%H:%M")}')
    start_task += timedelta(minutes=55)
