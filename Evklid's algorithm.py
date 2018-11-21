def gcd(a, b):
    if a == b:
        return a
    elif a > b:
        return gcd(a - b, b)
    else:
        return gcd(a, b - a)


print(gcd(12555, 313875))


def gcd_m(a, b):
    if b == 0:
        return a
    else:
        return gcd_m(b, a % b)


print(gcd_m(12555, 313875))


def gcd_m2(a, b):
    return a if b == 0 else gcd_m2(b, a % b)


print(gcd_m2(12555, 313875))
