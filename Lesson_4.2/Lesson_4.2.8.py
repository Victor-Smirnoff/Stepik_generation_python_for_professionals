import csv

with open('wifi.csv', 'r', encoding='utf-8') as my_file:
    content = [[row[1]] + [row[-1]] for row in csv.reader(my_file, delimiter=';')]

del content[0]
d = {}
for i in range(len(content)):
    if content[i][0] not in d.keys():
        d[content[i][0]] = int(content[i][1])
    else:
        d[content[i][0]] += int(content[i][1])

print(*[x[1] + ': ' + str(x[0]) for x in sorted(sorted(zip(d.values(), d.keys()), key=lambda x: x[1]), key=lambda x: x[0], reverse=True)], sep='\n')
