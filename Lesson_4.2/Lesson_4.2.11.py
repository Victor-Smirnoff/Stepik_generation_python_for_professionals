import csv

def condense_csv(filename, id_name):
    with open(filename, 'r', encoding='utf-8') as my_file:
        rows = csv.reader(my_file, delimiter=',')
        content = [row for row in rows]

    first = [id_name] + [content[i][1] for i in range(len(content)) if content[i][0] == content[0][0]]

    res = []
    for i in range(len(content)):
        if content[i][0] not in res:
            res.append(content[i][0])
            res.append(content[i][2])
        else:
            res.append(content[i][2])

    res2 = []

    while len(res):
        res2.append(res[:len(first)])
        res = res[len(first):]

    first = ','.join(first)
    res3 = [','.join(res2[i]) for i in range(len(res2))]

    with open('condensed.csv', 'w', encoding='utf-8') as output_file:
        print(first, file=output_file)
        for x in res3:
            print(x, file=output_file)
