from datetime import datetime, timedelta

print((datetime.strptime(input(), '%H:%M:%S') + timedelta(seconds=int(input()))).strftime('%H:%M:%S'))




