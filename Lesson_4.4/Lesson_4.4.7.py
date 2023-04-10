import json

with open('data.json', 'r', encoding='UTF-8') as my_file:
    data = json.load(my_file)

res = []

for i in range(len(data)):
    if type(data[i]) == str:
        data[i] += '!'
        res.append(data[i])
        continue
    if type(data[i]) in (int, float):
        data[i] += 1
        res.append(data[i])
        continue
    if type(data[i]) == bool:
        data[i] = not data[i]
        res.append(data[i])
        continue
    if type(data[i]) == list:
        data[i] *= 2
        res.append(data[i])
        continue
    if type(data[i]) == dict:
        data[i]["newkey"] = None
        res.append(data[i])
        continue
    if data[i] == None:
        continue


with open('updated_data.json', 'w', encoding='UTF-8') as output_file:
    json.dump(res, output_file, indent=3)
