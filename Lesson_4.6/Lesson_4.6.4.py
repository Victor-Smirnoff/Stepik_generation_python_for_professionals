import pickle


filename, number = input(), int(input())

with open(filename, 'rb') as file:
    content = pickle.load(file)

def func(elem):
    return type(elem) == int

if type(content) == dict:
    if len(list(filter(func, content))) == 0:
        res = 0
    else:
        res = sum(list(filter(func, content)))
    print('Контрольные суммы совпадают' if res == number else 'Контрольные суммы не совпадают')

if type(content) == list:
    if len(list(filter(func, content))) == 0:
        res = 0
        print('Контрольные суммы совпадают' if res == number else 'Контрольные суммы не совпадают')
    else:
        res = list(filter(func, content))
        print('Контрольные суммы совпадают' if max(res) * min(res) == number else 'Контрольные суммы не совпадают')
