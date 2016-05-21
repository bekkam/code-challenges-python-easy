"""Given list of ints, return list of *indices* of even numbers in list.

For example::

    >>> show_evens1([])
    []

    >>> show_evens1([2])
    [0]

    >>> show_evens1([1, 2, 3, 4])
    [1, 3]

"""

# Solution 1
# 1.75211405754
def show_evens1(nums):
    """Given list of ints, return list of *indices* of even numbers in list."""

    even_indices = []

    for i, num in enumerate(nums):
        if num % 2 == 0:
            even_indices.append(i)

    return even_indices

# Solution 2 (HB)
# 1.84735798836
def show_evens2(nums):
    """Given list of ints, return list of *indices* of even numbers in list."""

    even_indices = []

    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            even_indices.append(i)

    return even_indices


if __name__ == '__main__':
    import doctest
    import timeit

    print(timeit.timeit("show_evens1([1,2,3,4])",
                        setup="from __main__ import show_evens1"))
    print(timeit.timeit("show_evens2([1,2,3,4])",
                        setup="from __main__ import show_evens2"))

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. EVENLY HANDLED!\n"