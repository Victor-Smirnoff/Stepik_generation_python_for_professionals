import json
import sys

data = json.loads(sys.stdin.read())

for key, value in data.items():
    if type(value) == list:
        value = ', '.join(map(str, value))
        print(f'{key}: {value}')
    else:
        print(f'{key}: {value}')
