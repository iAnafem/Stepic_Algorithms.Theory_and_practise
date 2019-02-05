def max_price(_len, array):
    prev = 0
    curr = array[0]
    for i in range(1, _len):
        prev, curr = curr, max(prev, curr) + array[i]
    return curr


def main():
    n = int(input())
    stairs = list(map(int, input().split()))
    print(max_price(n, stairs))


if __name__ == "__main__":
    main()
