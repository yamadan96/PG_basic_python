while True:
    a, b = list(map(int, input().split()))

    if a == 0 and b == 0:
        break
    else:
        if a < b:
            print(f"{a} {b}")
        else:
            print(f"{b} {a}")
