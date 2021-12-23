"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
        функция, которая принимает N целых чисел,
        и возвращает список квадратов этих чисел
        >>> power_numbers(1, 2, 5, 7)
        [1, 4, 25, 49]
    """

    return [i**2 for i in args]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if num % i == 0:
                return False

        return True

    return False


def filter_numbers(nums, option):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)
    >>> filter_numbers([1, 2, 3], ODD)
    [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    [2, 4]
     >>> filter_numbers([2, 3, 4, 5, 6, 7, 9, 13], PRIME)
    [2, 3, 5, 7, 13]
    """
    if option == ODD:
        return list(filter(lambda i: i % 2 != 0, nums))
    elif option == EVEN:
        return list(filter(lambda i: i % 2 == 0, nums))
    elif option == PRIME:
        return list(filter(lambda i: is_prime(i), nums))
