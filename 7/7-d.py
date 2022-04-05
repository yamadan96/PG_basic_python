n, m, l = list(map(int, input().split()))

a = [[0 for i in range(m)] for j in range(n)]
b = [[0 for i in range(l)] for j in range(m)]
c = [[0 for i in range(l)] for j in range(n)]

for i in range(0, n):
    a[i] = list(map(int, input().split()))

for i in range(0, m):
    b[i] = list(map(int, input().split()))

for i in range(0, n):
    for j in range(0, l):
        ans = 0
        for k in range(0, m):
            ans += a[i][k] * b[k][j]
        c[i][j] = ans

for i in range(0, n):
    for j in range(0, l):
        if j < l-1:
            print(f"{c[i][j]} ", end='')
        elif j == l-1:
            print(f"{c[i][j]}")
