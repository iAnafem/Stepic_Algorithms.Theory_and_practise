def edit_distance(s1, s2):
    m = len(s1)
    n = len(s2)
    array = [[0] * (n + 1) for item in range(m + 1)]
    for i in range(m + 1):
        array[i][0] = i
    for j in range(n + 1):
        array[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            array[i][j] = min(array[i][j - 1] + 1,
                              array[i - 1][j] + 1,
                              array[i - 1][j - 1] + (s1[i - 1] != s2[j - 1]))

    return array[m][n]


def main():
    string_1 = input()
    string_2 = input()
    print(edit_distance(string_1, string_2))


if __name__ == "__main__":
    main()
