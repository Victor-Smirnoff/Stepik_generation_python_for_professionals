import sys

data = [line.strip() for line in sys.stdin]

data_tema = [line for line in data[:-1] if data[-1] in line]

def get_end_element_in_list(lst):
    return lst[-1], lst[0][0]

data_for_sort = [line.split(' / ') for line in data_tema]
for x in data_for_sort:
    x[-1] = float(x[-1])

res = sorted(data_for_sort, key=get_end_element_in_list)

for x in res:
    print(x[0])
