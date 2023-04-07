B = 1
KB = 1024 * B
MB = 1024 * KB
GB = 1024 * MB
TB = 1024 * GB

with open('files.txt', 'r', encoding='utf-8') as my_file:
    content = [line.strip() for line in my_file.readlines()]

content = [x.split() for x in content]
type_of_files = []
for i in range(len(content)):
    a = content[i][0].split('.')
    type_of_files.append(a[1])
type_of_files = sorted(set(type_of_files))

for j in range(len(content)):
    if content[j][2] == 'B':
        content[j][1] = int(content[j][1]) * B
    elif content[j][2] == 'KB':
        content[j][1] = int(content[j][1]) * KB
    elif content[j][2] == 'MB':
        content[j][1] = int(content[j][1]) * MB
    elif content[j][2] == 'GB':
        content[j][1] = int(content[j][1]) * GB
    del content[j][2]

d = {}

for typ in type_of_files:
    if typ not in d.keys():
        d[typ] = []

for key in d:
    for c in range(len(content)):
        if '.' + key in content[c][0]:
            d[key].append(content[c])

for key in d:
    count = 0
    for i in range(len(d[key])):
        for j in range(len(d[key][i])):
            count += d[key][i][1]
    d[key].append(int(count / 2))

d_res = {}

for key in d:
    if key not in d_res.keys():
        d_res[key] = []

for key in d:
    for i in range(len(d[key]) - 1):
        d_res[key].append(d[key][i][0])
    d_res[key].append(d[key][-1])

for key in d_res:
    for i in range(len(d_res[key])):
        d_res[key][i] = str(d_res[key][i])

for key in d_res:
    d_res[key] = sorted(d_res[key])

for key in d_res:
    d_res[key][0] = int(d_res[key][0])

def convert_data_bytes(num: int):
    if 0 < num < 2**10:
        return str(num) + ' ' + 'B'
    elif 2**10 <= num < 2**20:
        return str(round(num / 2**10)) + ' ' + 'KB'
    elif 2**20 <= num < 2**30:
        return str(round(num / 2**20)) + ' ' + 'MB'
    elif 2**30 <= num < 2**40:
        return str(round(num / 2**30)) + ' ' + 'GB'


for key in d_res:
    print(*d_res[key][1:], sep='\n')
    print('----------')
    print(f'Summary: {convert_data_bytes(d_res[key][0])}')
    print()
