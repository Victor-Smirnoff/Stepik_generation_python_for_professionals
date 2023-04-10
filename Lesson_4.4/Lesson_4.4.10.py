import json

with open('countries.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

d = {}
for i in range(len(data)):
    if data[i]['religion'] not in d.keys():
        d[data[i]['religion']] = []
        d[data[i]['religion']].append(data[i]['country'])
    else:
        d[data[i]['religion']].append(data[i]['country'])

with open('religion.json', 'w', encoding='utf-8') as outputfile:
    json.dump(d, outputfile, indent=3)
