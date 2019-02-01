def binary_search(_array, i):
    left, right = 0, len(_array) - 1
    if len(_array) == 1:
        return 0
    while left <= right:
        m = (left + right) // 2

        if _array[m] == i:
            return m
        elif _array[m] < i:
            right = m - 1
        else:
            left = m + 1
    return left


def find_sequence(array, n):
    if len(array) <= 1:
        return 1, [1]
    indexes = [0] * n
    sequence = [array[0]]
    for i in range(1, n):
        _min = min(sequence)
        m_ind = sequence.index(_min)
        print("i = ", i)
        print("elem = ", array[i])
        print("min = ", _min)
        print("min_index = ", m_ind)
        if array[i] == _min:
            print("do first")
            sequence.append(array[i])
            indexes[i] = len(sequence) - 1
        elif m_ind != len(sequence) - 1 and sequence[m_ind + 1] <= array[i] < _min:
            print("do second")
            sequence[m_ind] = array[i]
            indexes[i] = sequence.index(array[i])
        elif array[i] < _min:
            print("do third")
            sequence.append(array[i])
            indexes[i] = sequence.index(array[i])
        elif array[i] > _min:
            print("do fourth")
            sequence[binary_search(sequence, array[i])] = array[i]
            indexes[i] = sequence.index(array[i])
        print(indexes, sequence)
    res = max(indexes)
    result = [0] * n
    for x in range(len(array) - 1, -1, -1):
        if indexes[x] == res:
            result[x] = x + 1
            res -= 1
        else:
            result[x] = -1
    final = []
    for i in result:
        if i != -1:
            final.append(i)

    return max(indexes) + 1, final


def main():
    n = int(input())
    lst = list(map(int, input().split()))
    length, res = find_sequence(lst, n)
    print(length)
    for x in res:
        print(x, end=" ")


if __name__ == "__main__":
    main()
