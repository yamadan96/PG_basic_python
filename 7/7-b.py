while True:
    n, x = list(map(int, input().split()))

    if n == 0 and x == 0:
        break

    ans = 0
    for i in range(1, n-1):
        for j in range(i+1, n):
            for k in range(j+1, n+1):
                if x == i+j+k:
                    ans += 1
    print(ans)
