def sum_list(num_list):
    """Return the sum of all numbers in list.

    >>> sum_list([5, 3, 6, 2, 1])
    17
    """

    result = 0
    for num in num_list:
        result += num

    return result

if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED.\n"
