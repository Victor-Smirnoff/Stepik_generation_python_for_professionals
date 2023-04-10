import json

with open('people.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

pattern = list(max(data, key=len).keys())

for i in range(len(data)):
    for key in pattern:
        if key not in data[i].keys():
            data[i][key] = None

with open('updated_people.json', 'w', encoding='utf-8') as output_file:
    json.dump(data, output_file, indent=3)
