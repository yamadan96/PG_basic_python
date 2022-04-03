n = 1
A = [0] * 1
while n > 0:
    n = int(input())
    A.append(n)

for i in range(1, len(A)):
    if A[i] != 0:
        print(f"Case {i}: {A[i]}")
