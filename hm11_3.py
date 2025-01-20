def is_even(number):
    """
    Функція еревіряє, чи є число парним не використовуючи ділення

    Args:
        number (int): ціле число

    Returns:
        bool: True - якщо число парне, False - якщо непарне.
    """
    return (number & 1) == 0


assert is_even(2494563894038 ** 2) == True, 'Test1'
assert is_even(1056897 ** 2) == False, 'Test2'
assert is_even(24945638940387 ** 3) == False, 'Test3'

print('OK')
