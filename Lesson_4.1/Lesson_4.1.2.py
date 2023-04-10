import sys
from datetime import datetime

pattertn = '%Y-%m-%d'

data = [datetime.strptime(line.strip(), pattertn) for line in sys.stdin]

res = max(data) - min(data)

print(res.days)
