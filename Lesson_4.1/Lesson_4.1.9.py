import sys

data = [int(line.strip()) for line in sys.stdin]

arif = False
geom = False

for i in range(len(data) - 1):
    d_geom = data[-1] / data[-2]
    if data[i+1] / data[i] == d_geom:
        geom = True
    else:
        geom = False
        break

for i in range(len(data) - 1):
    d_arif = data[-1] - data[-2]
    if data[i+1] - data[i] == d_arif:
        arif = True
    else:
        arif = False
        break

if not arif and not geom:
    print('Не прогрессия')
elif arif:
    print('Арифметическая прогрессия')
elif geom:
    print('Геометрическая прогрессия')
