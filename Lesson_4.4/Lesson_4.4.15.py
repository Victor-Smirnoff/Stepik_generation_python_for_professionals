import json


with open('food_services.json', 'r', encoding='UTF-8') as file:
    content = json.load(file)

res_d = {}
res_net = {}
for d in content:
    if d['District'] not in res_d:
        res_d[d['District']] = 1
    else:
        res_d[d['District']] += 1

    if d['IsNetObject'] == 'да' and d['OperatingCompany'] not in res_net:
        res_net[d['OperatingCompany']] = 1
    elif d['IsNetObject'] == 'да' and d['OperatingCompany'] in res_net:
        res_net[d['OperatingCompany']] += 1

for key, value in res_d.items():
    if value == max(res_d.values()):
        max_food = f'{key}: {value}'

for key, value in res_net.items():
    if value == max(res_net.values()):
        max_net = f'{key}: {value}'

print(max_food)
print(max_net)
