card = [[False for i in range(13)] for j in range(4)]
pattern = ['S', 'H', 'C', 'D']

n = int(input())
for i in range(0, n):
    m, h = list(map(str, input().split()))
    card[pattern.index(m)][int(h)-1] = True

for i in range(0, 4):
    for j in range(0, 13):
        if card[i][j] == False:
            print(f"{pattern[i]} {j+1}")
