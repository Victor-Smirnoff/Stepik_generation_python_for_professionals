import sys

data = [int(line.strip()) for line in sys.stdin]

print('Дима' if data[-1] % 2 == 0 and len(data) % 2 == 0 or data[-1] % 2 != 0 and len(data) % 2 == 1 else 'Анри')
