def get_two_repeats(lst):
    return [x for x in set(lst) if lst.count(x) > 1]


lst = [int(x) for x in input().split()]

print(*get_two_repeats(lst))
