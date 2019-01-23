A = [1, 4, 5, 6, -4, 3, 3, 4, -45, 5, 6, 7, -8, 6, 5, 4, -4]

N = len(A)

for top in range(1, N):
    k = top
    print(k)
    while k > 0 and A[k-1] > A[k]:
        A[k], A[k-1] = A[k-1], A[k]
        k -= 1
print(A)
