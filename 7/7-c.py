r, c = list(map(int, input().split()))

field = [[0 for i in range(c)] for j in range(r)]
ans = [[0 for i in range(c+1)] for j in range(r+1)]

for i in range(0, r):
    field[i] = list(map(int, input().split()))

    for j in range(0, c):
        ans[i][j] = field[i][j]
        ans[r][j] += field[i][j]

for i in range(0, r+1):
    for j in range(0, c+1):
        if j < c:
            print(f"{ans[i][j]} ", end='')
        elif j == c:
            print(f"{sum(ans[i])}")
