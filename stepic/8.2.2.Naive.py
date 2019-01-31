def find_sequence(array, n):
    seq_array = [0] * n
    for i in range(0, n):
        seq_array[i] = 1
        for j in range(0, i):
            if array[j] >= array[i] and seq_array[j] + 1 > seq_array[i]:
                seq_array[i] = seq_array[j] + 1
    _length = max(seq_array)
    result = [-1] * n
    for i in range(len(seq_array) - 1, -1, -1):
        if seq_array[i] == _length:
            result[i] = i + 1
            _length -= 1
    final = []
    for i in result:
        if i != -1:
            final.append(i)
    return max(seq_array), final


def main():
    n = int(input())
    lst = list(map(int, input().split()))
    length, res = find_sequence(lst, n)
    print(int(length))
    for x in res:
        print(int(x), end=" ")


if __name__ == "__main__":
    main()
