W, H, x, y, r = list(map(int, input().split()))

if 0 <= x-r and x+r <= W and 0 <= y-r and y+r <= H:
    print("Yes")
else:
    print("No")
