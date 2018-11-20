A = [1, 4, 5, 6, -4, 3, 3, 4, -45, 5, 6, 7, -8, 6, 5, 4, -4]

N = len(A)

for pos in range(0, N-1):
    for k in range(pos+1, N):
        if A[k] < A[pos]:
            A[k], A[pos] = A[pos], A[k]

print(A)
