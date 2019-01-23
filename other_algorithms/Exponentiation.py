def pow_1(a, n):
    if n == 0:
        return 1
    elif n % 2 == 1:
        return pow(a, n - 1) * a
    else:
        return pow(a ** 2, n//2)


print(pow_1(5, 100000))


def pow_low(a, n):
    if n == 0:
        return 1
    else:
        return pow(a, n - 1) * a


print(pow_low(5, 100000))
