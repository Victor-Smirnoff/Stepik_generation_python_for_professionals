def csv_columns(filename):
    with open(filename, 'r', encoding='UTF-8') as my_file:
        content = [line.strip().split(',') for line in my_file.readlines()]

    d = {}
    for i in range(1, len(content)):
        for j in range(len(content[i])):
            if content[0][j] not in d.keys():
                d[content[0][j]] = []
                d[content[0][j]].append(content[i][j])
            else:
                d[content[0][j]].append(content[i][j])

    return d
