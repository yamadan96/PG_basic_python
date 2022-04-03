card = [[False for i in range(13)] for j in range(4)]
pattern = ['S', 'H', 'C', 'D']

floor = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]

n = int(input())
for i in range(0, n):
    b, f, r, v = list(map(int, input().split()))
    floor[b-1][f-1][r-1] += v

for b in range(0, 4):
    for f in range(0, 3):
        for r in range(0, 10):
            if r == 9:
                print(f" {floor[b][f][r]}")
            else:
                print(f" {floor[b][f][r]}", end='')
    if b < 3:
        print(f"####################")
