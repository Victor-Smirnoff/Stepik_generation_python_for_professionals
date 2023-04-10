import csv

with open('prices.csv', 'r', encoding='utf-8') as my_file:
    rows = csv.reader(my_file, delimiter=';')
    content = [row for row in rows]

tmp_min, tov_min, mag_min = 10**6, 0, 0

for i in range(1, len(content)):
    for j in range(1, len(content[i])):
        if int(content[i][j]) < tmp_min:
            tmp_min = int(content[i][j])
            tov_min = content[0][j]
            mag_min = content[i][0]
        elif content[i][j] == tmp_min:
            if content[0][j] < tov_min:
                tov_min = content[0][j]

print(f'{tov_min}: {mag_min}')
