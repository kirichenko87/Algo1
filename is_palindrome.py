def is_palindrome(value: int)-> bool:

    if not isinstance(value, int):
        raise TypeError

    if value < 0:
        return False

    old_value = value
    new_value = 0

    while value !=0:
        new_value += value % 10
        new_value *=10
        value //= 10

    return  old_value == new_value//10



print(is_palindrome(-121))



