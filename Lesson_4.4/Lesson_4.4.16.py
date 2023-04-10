import json


with open('food_services.json', 'r', encoding='UTF-8') as file:
    content = json.load(file)

d_res = {}

for d in content:
    if d['TypeObject'] not in d_res:
        d_res[d['TypeObject']] = [d['Name'], d['SeatsCount']]
    else:
        if d_res[d['TypeObject']][1] < d['SeatsCount']:
            d_res[d['TypeObject']] = [d['Name'], d['SeatsCount']]

sorted_keys = sorted(d_res.keys())

for value in sorted_keys:
    print(f'{value}: {d_res[value][0]}, {d_res[value][1]}')
