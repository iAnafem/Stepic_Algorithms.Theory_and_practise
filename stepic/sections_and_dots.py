n = int(input())
lines = sorted([[*map(int, input().split())] for i in range(n)], key=lambda x: x[1])
section, result = 0, [lines[0][1]]
while section < n:
    if lines[section][0] <= result[-1]:
        section += 1
    else:
        result.append(lines[section][1])
print(len(result))
print(*result)
