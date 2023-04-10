with open('deniro.csv', 'r', encoding='UTF-8') as my_file:
    content = [line.strip().split(',') for line in my_file.readlines()]

n = int(input())

for i in range(len(content)):
    for j in range(len(content[i])):
        if content[i][j].isdigit():
            content[i][j] = int(content[i][j])

res = sorted(content, key=lambda x: x[n - 1])

res2 = []
for i in range(len(res)):
    for j in range(len(res[i])):
        xt = ','.join(map(str, res[i]))
    res2.append(xt)

print(*res2, sep='\n')
