def is_three_sum_zero(some_array):
    """Return True if any three items in array sum to zero. Else False.

    >>> is_three_sum_zero([])
    False

    >>> is_three_sum_zero([1,2])
    False

    >>> is_three_sum_zero([1, 2, 10, 4, -5, -12])
    True
    """

    some_array.sort()
    i = 0
    j = 1

    while i < len(some_array) - 3:
        while j < len(some_array) - 2:
            k = len(some_array) - 1
            while k > j:
                if some_array[i] + some_array[j] + some_array[k] == 0:
                    return True
                else:
                    k -= 1
            j += 1
        i += 1

    return False


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n**** ALL TESTS PASSED.\n"
