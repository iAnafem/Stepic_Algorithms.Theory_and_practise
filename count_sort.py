A = [1, 4, 5, 6, 4, 3, 3, 4, 5, 5, 6, 8, 6, 5, 4, 4, 0, 5, 8, 7, 1, 9, 9, 9, 2, 4, 3, 5, -1, -2, -1, -4, -6, -4, -3]


m1 = max(A)
m2 = min(A)
scope = m1 - m2 + 1
F = [0] * scope
for x in A:
    F[x] += 1
A[:] = []
for number in range(m2, m1+1):
    A += [number] * F[number]

print(A)
