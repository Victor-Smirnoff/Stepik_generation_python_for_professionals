n = int(input())
lst = [input().split(', ') for _ in range(n)]
res_lst = []
for x in lst:
    res_lst += x
set_lst = set(res_lst)
itog = []
for lang in set_lst:
    if res_lst.count(lang) == n:
        itog.append(lang)
itog = sorted(itog)

if len(itog) != 0:
    outpu = ', '.join(itog)
    print(outpu)
else:
    print('Сериал снять не удастся')
