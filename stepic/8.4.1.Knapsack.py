def get_price(cap, q, _weight):
    array = [[0] * (cap + 1) for _ in range(q + 1)]
    for i in range(1, q + 1):
        for w in range(1, cap + 1):
            array[i][w] = array[i - 1][w]
            if _weight[i - 1] <= w:
                array[i][w] = max(array[i][w], array[i-1][w - _weight[i - 1]] + _weight[i - 1])
    print(array)
    return array[-1][-1]


def main():
    capacity, quantity = map(int, input().split())
    weight = list(map(int, input().split()))
    print(get_price(capacity, quantity, weight))


if __name__ == "__main__":
    main()
