"""Calculate possible change from combinations of dimes and pennies.

Given an infinite supply of dimes and pennies, find the different
amounts of change can be created with exact `num_coins` coins?

For example, when num_coins = 3, you can create:

    3 = penny + penny + penny
   12 = dime + penny + penny
   21 = dime + dime + penny
   30 = dime + dime + dime

For example:

    >>> coins(0) == {0}
    True

    >>> coins(1) == {1, 10}
    True

    >>> coins(2) == {2, 11, 20}
    True

    >>> coins(3) == {3, 12, 21, 30}
    True

    >>> coins(4) == {4, 13, 22, 31, 40}
    True

    >>> coins(10) == {10, 19, 28, 37, 46, 55, 64, 73, 82, 91, 100}
    True
"""


def coins(num_coins):
    """Find change from combinations of `num_coins` of dimes and pennies.

    This should return a set of the unique amounts of change possible.
    """

    # total change = num_of_dimes * 10 + num_of_pennies * 1
    # start will all pennies
    # sum all pennies and add to result_set
    # subtract 1 from last item in result set, add 10, and add this amount to result set

    if num_coins == 0:
        return {0}

    PENNY = 1
    DIME = 10

    prev = num_coins * PENNY
    result = {prev}

    for count in range(0, num_coins):
        prev = (prev - PENNY + DIME)
        result.add(prev)
        count += 1

    return result

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU CAN TAKE THAT TO THE BANK!\n"
