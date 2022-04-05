def PointCheck(m, f, r):
    if m == -1 and f == -1 and r == -1:
        return 'End'
    elif m == -1 or f == -1:
        return 'F'

    if m == -1:
        m = 0
    if f == -1:
        f = 0

    if m+f >= 80:
        return 'A'
    elif m+f >= 65:
        return 'B'
    elif m+f >= 50:
        return 'C'
    elif m+f >= 30 and r >= 50:
        return 'C'
    elif m+f >= 30:
        return 'D'
    else:
        return 'F'


while True:
    m, f, r = list(map(int, input().split()))

    ans = PointCheck(m, f, r)

    if ans == "End":
        break
    print(ans)
