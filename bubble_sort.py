A = [1, 4, 5, 6, -4, 3, 3, 4, -45, 5, 6, 7, -8, 6, 5, 4, -4]

N = len(A)

for bypass in range(1, N):
    for k in range(0, N-bypass):
        if A[k] > A[k+1]:
            A[k], A[k+1] = A[k+1], A[k]
        print(A, k, k+1)
print(A)
