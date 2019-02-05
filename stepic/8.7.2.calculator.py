# put your python code here
n = int(input())
# находим наименьшее число шагов
D = [0] * n
for i in range(1, n):
    if (i + 1) % 3. == 0:
        D[i] = D[(i + 1)//3-1]+1
    elif (i + 1) % 2. == 1:
        D[i] = D[(i - 1)]+1
    else:
        D[i] = min(D[(i - 1)], D[(i + 1)//2-1])+1

# находим последовательность чисел
sequence = [1] * (D[n-1]+1)
sequence[D[n - 1]] = n
curr = n - 1
prev = 0
for s in range(1, D[n-1]):
    i = D[n-1] - s
    if (curr + 1) % 3 == 0 and D[int(curr)] == D[int((curr+1)//3-1)]+1:
        prev = (curr+1)/3-1
        sequence[i] = int(sequence[i+1]/3.)
    elif (curr + 1) % 2 == 0 and D[int(curr)] == D[int((curr+1)//2-1)]+1:
        prev = (curr+1)/2-1
        sequence[i] = int(sequence[i+1]/2.)
    else:
        prev = curr-1
        sequence[i] = sequence[i+1]-1
    curr = prev
print(D[n-1])
print(' '.join(map(str, sequence)))
