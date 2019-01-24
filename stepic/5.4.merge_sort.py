def merge_sort(_array):
    count = 0
    if len(_array) > 1:
        mid = len(_array)//2
        left_half = _array[:mid]
        right_half = _array[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                _array[k] = left_half[i]
                i += 1
            else:
                _array[k] = right_half[j]
                j += 1

            k += 1

        while i < len(left_half):
            _array[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            _array[k] = right_half[j]
            j += 1
            k += 1
            count += 1
    return count


n = int(input())
A = list(map(int, input().split(" ")))
print(merge_sort(A))
