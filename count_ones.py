def count_ones(value: int) ->int:
    if not isinstance(value, int):
        raise TypeError

    if value < 0:
        raise ValueError

    count_one = 0
    while value!=0:

        ost = value % 2
        if ost == 1:
            count_one += 1
        value //= 2

    return count_one

print(count_ones(1234123))