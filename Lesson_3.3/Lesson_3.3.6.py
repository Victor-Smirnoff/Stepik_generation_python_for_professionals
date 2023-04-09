from datetime import datetime

with open('diary.txt', 'r', encoding='utf-8') as my_file:
    content = [line.split('\n\n') for line in my_file.readlines()]

content[-1][0] = content[-1][0] + '\n'
content.append(['\n'])
content = [line[0] for line in content]

tmp = []
for i in range(len(content)):
    if '.2008' in content[i]:
        tmp.append(i)

d = {}
for x in range(len(tmp)):
    if tmp[x] != tmp[-1]:
        d[content[tmp[x]].replace('\n', '')] = content[tmp[x]:tmp[x+1]]
    else:
        d[content[tmp[x]].replace('\n', '')] = content[tmp[x]:]

d_keys = list(d.keys())

def get_seconds(datetime_str):
    my_date = datetime.strptime(datetime_str, '%d.%m.%Y; %H:%M')
    quantity_of_seconds = my_date.timestamp()
    return quantity_of_seconds

d_keys = sorted(d_keys, key=get_seconds)

d[d_keys[-1]].remove('\n')
d[d_keys[-1]][-1] = d[d_keys[-1]][-1].replace('\n', '')

for key in d_keys:
    print(*d[key], sep='', end='')
