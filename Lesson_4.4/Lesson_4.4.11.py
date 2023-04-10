import csv
import json


with open('playgrounds.csv', 'r', encoding='UTF-8') as my_file:
    content = csv.DictReader(my_file, delimiter=';', quotechar='"')
    d = {}
    for row in content:
        if row['AdmArea'] not in d:
            d[row['AdmArea']] = {row['District']: []}
            d[row['AdmArea']][row['District']].append(row['Address'])
        else:
            if row['District'] not in d[row['AdmArea']]:
                d[row['AdmArea']][row['District']] = []
                d[row['AdmArea']][row['District']].append(row['Address'])
            else:
                d[row['AdmArea']][row['District']].append(row['Address'])

with open('addresses.json', 'w', encoding='UTF-8') as my_output_file:
    json.dump(d, my_output_file, indent=3, ensure_ascii=False)
