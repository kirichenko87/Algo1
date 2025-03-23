def fibonacci(value: int) -> list:
    if not isinstance(value, int):
        raise TypeError

    if value < 0:
        raise ValueError

    if value == 0:
        return [0]

    num1 = 0
    num2 = 1
    lst_fib = [0, 1]

    for i in range(0, value - 1, 1):
        num3 = num1 + num2
        num1 = num2
        num2 = num3
        lst_fib.append(num3)

    return lst_fib


print(fibonacci(100))