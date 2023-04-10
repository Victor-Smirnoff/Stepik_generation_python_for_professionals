import json

with open('data1.json', 'r', encoding='utf-8') as file_1:
    data_1 = json.load(file_1)

with open('data2.json', 'r', encoding='utf-8') as file_2:
    data_2 = json.load(file_2)

data_total = data_1 | data_2

with open('data_merge.json', 'w', encoding='utf-8') as output_file:
    json.dump(data_total, output_file, indent=3)
