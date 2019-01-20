n = int(input())
result = []
if n == 1:
    print("1 \n 1")
elif n == 2:
    print("1 \n 2")
else:
    for i in range(1, n):
        if i <= n:
            n -= i
            result.append(i)
        else:
            result[-1] += n
            break
print(len(result))
print(*result)

