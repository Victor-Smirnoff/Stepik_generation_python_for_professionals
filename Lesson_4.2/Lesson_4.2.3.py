with open('sales.csv', 'r', encoding='UTF-8') as my_file:
    content = [line.strip().split(';') for line in my_file.readlines()]

del content[0]

res = [content[i][0] for i in range(len(content)) if int(content[i][1]) > int(content[i][2])]

print(*res, sep='\n')
