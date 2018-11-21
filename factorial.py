def f(n):
    assert n >= 0, "Факториал отрицательного числа не определен"
    if n == 0:
        return 1
    return f(n-1)*n


print(f(5))
