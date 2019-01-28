import random


def get_separator(_array):
    return random.choice(_array)


def quick_sort(_array, fst, lst):
    if fst >= lst:
        return

    i, j = fst, lst
    pivot = get_separator(_array)

    while i <= j:
        while _array[i] < pivot:
            i += 1
        while _array[j] > pivot:
            j -= 1
        if i <= j:
            _array[i], _array[j] = _array[j], _array[i]
            i, j = i + 1, j - 1
    quick_sort(_array, fst, j)
    quick_sort(_array, i, lst)


def binary_search(_array, point):
    left = 0
    right = len(_array) - 1
    while left <= right:
        mid = (left + right) // 2
        if _array[mid] == point:
            while _array[mid + 1] == point:
                mid += 1
            return mid + 1
        elif _array[mid] > point:
            right = mid - 1
        elif _array[mid] < point:
            if _array[mid + 1] > point:
                return mid + 1
            left = mid + 1


def solution(_starts, _ends, _points):
    quick_sort(_starts, 0, len(_starts) - 1)
    quick_sort(_ends, 0, len(_ends) - 1)
    result = []
    for item in _points:
        count1 = binary_search(_starts, item)
        count2 = binary_search(_ends, item)

        print(count1, count2)



def main():
    n, m = map(int, input().split())
    starts = []
    ends = []
    for i in range(n):
        segments = list(map(int, input().split(" ")))
        starts.append(segments[0])
        ends.append(segments[1])
    points = list(map(int, input().split(" ")))
    print(" ".join([str(count) for count in solution(starts, ends, points)]))




if __name__ == "__main__":
    main()
