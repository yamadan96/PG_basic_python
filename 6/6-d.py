n, m = list(map(int, input().split()))

A = [[0 for i in range(m)] for j in range(n)]
B = [0 for i in range(m)]

for i in range(0, n):
    a = list(map(int, input().split()))

    for j in range(m):
        A[i][j] = a[j]

for i in range(0, m):
    b = int(input())
    B[i] = b

for i in range(0, n):
    ans = 0
    for j in range(0, m):
        ans += A[i][j] * B[j]
    print(ans)
