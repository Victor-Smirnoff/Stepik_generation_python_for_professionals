from zipfile import ZipFile
import json


def is_correct_json(string):
    try:
        if json.loads(string):
            return True
    except:
        return False

with ZipFile('data.zip') as zip_file:
    info = zip_file.infolist()
    res = [info[i] for i in range(len(info)) if info[i].filename.split('.')[-1] == 'json']
    for i in range(len(res)):
        zip_file.extract(res[i].filename)

lst = []

for i in range(len(res)):
    with open(res[i].filename, 'r', encoding='utf-8') as file:
        try:
            content = ' '.join([x.strip() for x in file.readlines()])
            if is_correct_json(content):
                x = json.loads(content)
                if x['team'] == 'Arsenal':
                    lst.append([x['first_name'], x['last_name']])
        except:
            pass

lst = sorted(lst, key=lambda x: (x[0], x[1]))

for player in lst:
    print(f'{player[0]} {player[1]}')
