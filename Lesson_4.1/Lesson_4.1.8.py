import sys
from datetime import datetime

data = [datetime.strptime(line.strip(), '%d.%m.%Y') for line in sys.stdin]

if data == sorted(set(data)):
    print('ASC')
elif data == sorted(set(data), reverse=True):
    print('DESC')
else:
    print('MIX')
