n, capacity = map(int, input().split())
items = [[*map(int, input().split())] for i in range(n)]
items_mod = [(items[j][0] / items[j][1], items[j][1]) for j in range(len(items))]
items_mod.sort(reverse=True)
result = 0
for price, w in items_mod:
    if w < capacity:
        capacity -= w
        result += price * w
    else:
        result += price * capacity
        break
print("{:.3f}".format(result))
