def find_sequence(array, n):
    seq_array = [0] * n
    for i in range(0, n):
        seq_array[i] = 1
        for j in range(0, i):
            if array[j] <= array[i] and seq_array[j] + 1 > seq_array[i] and array[i] % array[j] == 0:
                seq_array[i] = seq_array[j] + 1
    return max(seq_array)


def main():
    n = int(input())
    lst = list(map(int, input().split()))
    print(find_sequence(lst, n))


if __name__ == "__main__":
    main()

