"""Find the subsequence with the largest sum.

Given a list of integers, like:

  [1, 0, 3, -8, 4, -2, 3]

Return the contiguous subsequence with the largest sum. For
that example, the answer would be [4, -2, 3], which sums to 5.


    >>> largest_sum([1, 0, 3, -8, 4, -2, 3])
    [4, -2, 3]

    >>> largest_sum([1, 0, 3, -8, 4, -2, 3, -2])
    [4, -2, 3]

    >>> largest_sum([1, 0, 3, -8, 19, -20, 4, -2, 3, -2])
    [19]

For ties, return the first one:

    >>> largest_sum([2, 2, -10, 1, 3, -20])
    [2, 2]

Return the shortest version:

    >>> largest_sum([2, -2, 3, -1])
    [3]

If the list is all negative numbers, the subsequence
with the highest sum will be empty (ie, we can do no better
than pick nothing!):

    >>> largest_sum([-1, -2])
    []
"""


def largest_sum(nums):
    """Find subsequence with largest sum."""

    """
    The max subarray is the greater of: the sum of prev subarray, or the sum of
    the subarray at the current position.
    The start index is reset to current position whenever the current position
    causes the sum of the array to go negative.
    """
    def get_largest_sum(max_sum, array, start, end, max_start, max_stop):

        # base case: we're at the end of the array
        if end > len(nums):
            return nums[max_start: max_stop]

        # if current subseqence is greater than max_sum, save its sum as the new
        # max_sum, and save its start and endpoints
        if sum(array[start:end]) > max_sum:
            max_sum = sum(array[start:end])
            max_start = start
            max_stop = end

        # if sum of current sequence is <= 0, reset the start position
        if sum(array[start:end]) <= 0:
            start = end

        return get_largest_sum(max_sum, array, start, end + 1, max_start, max_stop)

    return get_largest_sum(0, nums, 0, 0, 0, 0)


# ###################################################################
# HB solution

def largest_sum(nums):
    """Find subsequence with largest sum."""

    # START SOLUTION

    # Our best (update as we find new bests)
    best_sum = 0
    start_of_best = 0
    end_of_best = -1  # (nothing)

    # Current sum and start
    current_sum = 0
    start_of_curr = 0

    for i, n in enumerate(nums):
        current_sum += n

        if current_sum > best_sum:
            # Best so far -- record this sum & its start and end
            best_sum = current_sum
            start_of_best = start_of_curr
            end_of_best = i

        if current_sum <= 0:
            # Dropped belonw 1, so we can't improve -- reset
            # start_of_best, to begin with next number
            start_of_curr = i + 1
            current_sum = 0

    return nums[start_of_best:end_of_best + 1]

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU HANDLED THIS SUMMARILY!\n"
