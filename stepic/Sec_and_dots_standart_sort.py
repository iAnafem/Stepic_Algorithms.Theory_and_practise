def bin_sch(v, elem):
    l = answer = 0
    r = len(v) - 1
    while (l <= r):
        m = (l+r)//2
        if v[m] <= elem:
            answer = m+1
            l = m + 1
        else:
            r = m - 1
    return answer


a = []
b = []
n = int(input().split()[0])
for i in range(n):
    A, B = map(int, input().split())
    a.append(A)
    b.append(B)
a.sort()
b.sort()
p = [int(i) for i in input().split()]
for x in p:
    print(bin_sch(a, x) - bin_sch(b, x-1), end=' ')
