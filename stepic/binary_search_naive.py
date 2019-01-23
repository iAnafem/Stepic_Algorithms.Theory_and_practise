def binary_search(_numbers, _item):
    if _item in _numbers:
        res = _numbers.index(_item) + 1
    else:
        res = -1
    return res


def main():
    numbers = list(map(int, input().split(" ")))[1:]
    search = list(map(int, input().split(" ")))[1:]
    result = [str(binary_search(numbers, item)) for item in search]
    print(" ".join(result))


if __name__ == "__main__":
    main()
