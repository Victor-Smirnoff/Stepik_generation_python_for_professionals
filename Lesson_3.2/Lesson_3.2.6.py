from datetime import date
n = int(input())
dates = sorted([date.fromisoformat(input()) for _ in range(n)])

for d in dates:
    print(d.strftime('%d/%m/%Y'))
