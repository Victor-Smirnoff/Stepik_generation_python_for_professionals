from datetime import date

def is_correct(day, month, year):
    try:
        date(year, month, day)
        return True
    except:
        return False


s = input()

coont = 0

while s != 'end':
    s = list(map(int, s.split('.')))
    if is_correct(s[0], s[1], s[2]) == True:
        coont += 1
        print('Корректная')
    else:
        print('Некорректная')
    s = input()

print(coont)
