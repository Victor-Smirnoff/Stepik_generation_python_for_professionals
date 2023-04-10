import csv

with open('titanic.csv', 'r', encoding='utf-8') as my_file:
    content = [row for row in csv.reader(my_file, delimiter=';')]

del content[0]
print(*[row[1] for row in [row for row in content if row[0] == '1' and float(row[3]) < 18.0] if row[2] == 'male'] + [row[1] for row in [row for row in content if row[0] == '1' and float(row[3]) < 18.0] if row[2] == 'female'], sep='\n')
