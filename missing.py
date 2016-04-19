"""Given a list of numbers 1...max_num, find which one is missing in a list."""


def missing_number(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing.

    *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list
    """

    # create a set of nums, one to max num
    # sum the set
    # sum nums
    # return set_sum - sum_nums

    consecutive_nums = range(1, max_num + 1)
    return sum(consecutive_nums) - sum(nums)

print missing_number([2, 1, 4, 3, 6, 5, 7, 10, 9], 10)
# if __name__ == '__main__':
#     import doctest
#     if doctest.testmod().failed == 0:
#         print "\n*** ALL TESTS PASS. NICELY DONE!\n"
