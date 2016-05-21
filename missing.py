import math
"""Given a list of numbers 1...max_num, find which one is missing in a list."""

# ######################### Part 1: Simple Solution:
# O(N)
# Additional storage

# Solution A:
# 1.52021002769
def missing_number1(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing.

    *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list
    """

    all_nums = sum(range(max_num + 1))
    return all_nums - sum(nums)

# Solution B (HB)
# 2.55650806427
def missing_number_scan(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing.

    *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list

    >>> missing_number_scan([1, 2, 3, 4, 5, 6, 7, 9, 10], 10)
    8
    """

    # 1st solution: Initial solution: keep track of what you've
    #               seen in a separate list

    seen = [False] * max_num

    for n in nums:
        seen[n - 1] = True

    # The False value is the one we haven't seen

    return seen.index(False) + 1

############################### Part 2: Sorting
# O(N log N)
# No additional storage

# Solution A
# Runtime: N log N
# 1.02051496506
def missing_number2(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing.

    *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list
    """

    nums.sort()
    i = 1
    while i <= len(nums):
        if nums[i] != i:
            return i

# Solution B (HB)
# Runtime: N log N
# 2.18603801727
def missing_number_sort(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing.

    *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list

    >>> missing_number_sort([1, 2, 3, 4, 5, 6, 7, 9, 10], 10)
    8
    """

    # 2nd solution: if we can't create another data structure
    #               sort and scan for missing number

    nums.append(max_num + 1)
    nums.sort()
    last = 0

    for i in nums:
        if i != last + 1:
            return last + 1
        last += 1

    raise Exception("None are missing!")

##################################### Part 3: Math Solution
# Solution A
# Runtime: O(N)
# 1.52231311798
def missing_number3(nums, max_num):

    # expected_factorial = math.factorial(max_num)

    nums_factorial = 1

    for num in nums:
        nums_factorial *= num

    return math.factorial(max_num)/nums_factorial

# Solution B (HB)
# 1.49855422974
def missing_number_sum(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing.

    *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list

    >>> missing_number_sum([1, 2, 3, 4, 5, 6, 7, 9, 10], 10)
    8
    """

    # 3rd solution: find missing number by comparing expected sum vs actual

    expected = sum(range(max_num + 1))

    # Alternatively, there's a math formula that finds the sum of 1..n
    # https://en.wikipedia.org/wiki/Arithmetic_progression#Sum
    #
    # expected = ( n + 1 ) * ( n / 2 )
    #
    # This makes this problem O(1) !

    return expected - sum(nums)

if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASS. NICELY DONE!\n"
