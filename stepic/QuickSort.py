import random


def get_separator(_array):
    separator = random.choice(_array)
    sep_index = _array.index(separator)
    return separator, sep_index


def quick_sort(_array, l, r):
    sep, sep_index = get_separator(_array)
    print(sep)
    _array[0], _array[sep_index] = _array[sep_index], _array[0]
    print(_array)
    j = 1
    print(l, r)
    for i in range(l + 1, r + 1):
        if _array[i] < sep:
            _array[i], _array[j] = _array[j], _array[i]
            j += 1
            print(_array)
        elif _array[i] > sep:
            print(_array)
            continue
        elif _array[i] == sep:
            continue

    _array[0], _array[j - 1] = _array[j - 1], _array[0]
    return _array, j


def solution(_starts, _ends, _points):
    return []


def main():
    n, m = map(int, input().split())
    starts = []
    ends = []
    for i in range(n):
        segments = list(map(int, input().split(" ")))
        starts.append(segments[0])
        ends.append(segments[1])
    points = list(map(int, input().split(" ")))
    #print(" ".join([str(count) for count in solution(starts, ends, points)]))
    print(quick_sort(starts, 0, len(starts) - 1))


if __name__ == "__main__":
    main()
