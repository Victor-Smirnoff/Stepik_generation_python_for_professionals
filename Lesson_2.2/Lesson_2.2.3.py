n, X, Y, A, B = list(map(int, input().split()))
res1 = list(range(1, n + 1))
res2 = res1[X-1:Y]
res2 = res2[::-1]
res1 = res1[:X-1] + res2 + res1[Y:n+1]
res3 = res1[A-1:B]
res3 = res3[::-1]
res1 = res1[:A-1] + res3 + res1[B:n+1]

print(*res1)
