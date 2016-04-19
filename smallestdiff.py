"""Given two lists, find the smallest difference between any two nums.

For example, given the lists:

  {10, 20, 14, 16, 18}
  {30, 23, 54, 33, 96}

The result would be 3, since 23 - 20 = 3 is the smallest difference of
any pair of numbers in those lists.

IMPORTANT: you must solve this with an algorithm that is faster than
O(ab)---that is, you cannot compare each item of list a against
each item of list b (that would be O(ab) time).

Joel Burton <joel@joelburton.com>.

Adapted from a problem in `Cracking the Coding Interview, 6th Edition`.
Gayle Laakmann McDowell, Career Cup (Palo Alto, CA). 2015.
"""


def smallest_diff(a, b):
    """Return smallest diff between all items in a and b.

        >>> smallest_diff([10, 20, 30, 40], [15, 25, 33, 45])
        3
    """

    i = 0
    j = 0

    # initialize smallest_diff to the difference of a[0] and b[0]
    smallest_diff = abs(a[i] - b[j])

    while i < len(a) and j < len(b):
        # get the diff btwn a and b
        diff = abs(a[i] - b[j])
        # if its 0, return 0 (bc its the smallest possible diff)
        if diff == 0:
            return 0
        # if diff isnt 0, but is less than our current smallest_diff, set smallest diff to current diff
        if diff < smallest_diff:
            smallest_diff = diff
        # if a's current index is less than b's current index, go to the next item in list a. otherwise, go to next item in list b
        if min(a[i], b[j]) == a[i]:
            i += 1
        else:
            j += 1

    return smallest_diff


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. NICE WORK!\n"
