n = int(input())
A = list(map(int, input().split(" ")))
res = 0
for top in range(1, n):
    k = top
    while k > 0 and A[k-1] > A[k]:
        A[k], A[k-1] = A[k-1], A[k]
        res += 1
        k -= 1


print(A, res)
