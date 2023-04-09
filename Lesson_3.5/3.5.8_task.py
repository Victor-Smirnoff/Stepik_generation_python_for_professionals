from datetime import date, datetime, timedelta

def choose_plural(amount, declensions):
    if amount % 10 in (2, 3, 4) and amount % 100 not in range(12, 15):
        return str(amount) + ' ' + str(declensions[1])
    if amount % 10 in (5, 6, 7, 8, 9, 0) or amount % 100 in range(10, 21):
        return str(amount) + ' ' + str(declensions[2])
    if amount % 100 != 11 and amount % 10 == 1:
        return str(amount) + ' ' + str(declensions[0])


declensions_days = ('день', 'дня', 'дней')
declensions_hours = ('час', 'часа', 'часов')
declensions_minutes = ('минута', 'минуты', 'минут')

datetime_kurs = datetime.strptime('08.11.2022 12:00', '%d.%m.%Y %H:%M')
my_datetime = datetime.strptime(input(), '%d.%m.%Y %H:%M')

time_to_production = datetime_kurs - my_datetime
days_to_production = time_to_production.days
hours_to_production = time_to_production.seconds // 3600
minutes_to_production = (time_to_production.seconds // 60) % 60

if my_datetime >= datetime_kurs:
    print('Курс уже вышел!')
else:
    if days_to_production > 0 and hours_to_production > 0:
        print(f'До выхода курса осталось: {choose_plural(days_to_production, declensions_days)} и {choose_plural(hours_to_production, declensions_hours)}')
    elif days_to_production > 0 and hours_to_production == 0:
        print(f'До выхода курса осталось: {choose_plural(days_to_production, declensions_days)}')
    elif days_to_production == 0 and hours_to_production > 0 and minutes_to_production > 0:
        print(f'До выхода курса осталось: {choose_plural(hours_to_production, declensions_hours)} и {choose_plural(minutes_to_production, declensions_minutes)}')
    elif days_to_production == 0 and hours_to_production > 0 and minutes_to_production == 0:
        print(f'До выхода курса осталось: {choose_plural(hours_to_production, declensions_hours)}')
    elif days_to_production == 0 and hours_to_production == 0 and minutes_to_production > 0:
        print(f'До выхода курса осталось: {choose_plural(minutes_to_production, declensions_minutes)}')
