n = int(input())
lst_existing = [input() for _ in range(n)]

m = int(input())
lst_new = [input() for _ in range(m)]

for i in range(len(lst_new)):
    num = 1
    if lst_new[i] + '@beegeek.bzz' not in lst_existing:
        lst_existing.append(lst_new[i] + '@beegeek.bzz')
    elif lst_new[i] + '@beegeek.bzz' in lst_existing:
        if lst_new[i] + str(num) + '@beegeek.bzz' not in lst_existing:
            lst_existing.append(lst_new[i] + str(num) + '@beegeek.bzz')
        else:
            while lst_new[i] + str(num) + '@beegeek.bzz' in lst_existing:
                num += 1
                continue
            lst_existing.append(lst_new[i] + str(num) + '@beegeek.bzz')

print(*lst_existing[-m:], sep='\n')
