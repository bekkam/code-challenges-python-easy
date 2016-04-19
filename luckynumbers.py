"""Return n unique random numbers from 1-10 (inclusive).

Given the numbers 1-10, return `n` random numbers, making sure
to never return the same number twice. You can trust that this
function will never be called with n < 0 or n > 10.

It's tricky to test random functions! However, we can make sure
asking for zero numbers gives us an empty list::

    >>> lucky_numbers(0)
    []

And if we ask for all numbers, we shouldn't get any repeats::

    >>> sorted(lucky_numbers(10))
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""

import random


def lucky_numbers(n):
    """Return n unique random numbers from 1-10 (inclusive)."""

    # list solution -
    list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    result = []

    count = 0

    while count < n:
        last_index = len(list_num) - 1                     # get length --> O(1)
        index = random.randint(0, last_index)

        result.append(list_num[index])                     # append -> O(1), list_num[index] --> O(1)

        del list_num[index]                                # O(n)

        count += 1

    return result


def lucky_numbers(n):
    """Return n unique random numbers from 1-10 (inclusive)."""

    # list solution2, using l.remove (bc its O(n), same as del[index]
    nums = range(1, 11)
    result = []

    for i in range(n):
        num = random.choice(nums)
        result.append(num)
        nums.remove(num)

    return result

# print lucky_numbers(0)
if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT!\n"
