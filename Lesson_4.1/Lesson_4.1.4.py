import sys

data = [int(line.strip()) for line in sys.stdin]

print(f'Рост самого низкого ученика: {min(data)}\nРост самого высокого ученика: {max(data)}\nСредний рост: {sum(data) / len(data)}' if data else 'нет учеников')
