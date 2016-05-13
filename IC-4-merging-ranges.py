
# Runtime: N log N
# Runspace: N
def condense_meeting_times1(list_of_tuples_of_meeting_times):
    """Takes a list of meeting time tuples (start, end) and returns condensed
    list of tuples representing all non-overlapping ranges.

    >>> condense_meeting_times1([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
    [(0, 1), (3, 8), (9, 12)]

    >>> condense_meeting_times1([(1, 5), (2, 3)])
    [(1, 5)]

    >>> condense_meeting_times1([(1, 10), (2, 6), (3, 5), (7, 9)])
    [(1, 10)]

    >>> condense_meeting_times1([(1, 10), (2, 6), (3, 5), (1, 11), (7, 9), (1, 15)])
    [(1, 15)]

    >>> condense_meeting_times1([(1, 3), (2, 4)])
    [(1, 4)]

    >>> condense_meeting_times1([(1, 2), (2, 3)])
    [(1, 3)]
    """

    ######################### LEMMA: ########################################
    # Meetings "overlap" when current meeting starts before/at the
    # end of the meeting most recently added to result.
    ########################################################################

    # sort list of meetings by start time
    list_of_tuples_of_meeting_times.sort()

    # add first meeting to result
    result = [list_of_tuples_of_meeting_times[0]]

    for curr_start, curr_end in list_of_tuples_of_meeting_times[1:]:
        # tuple unpacking
        prev_start, prev_end = result[-1]

        # if current and prev meeting overlap: set the last tuple in result equal
        # to start of last meeting, and end at the latest running meeting of the two
        if curr_start <= prev_end:
            result[-1] = (prev_start, max(prev_end, curr_end))

        # if meetings dont overlap: add current meeting tuple to result
        else:
            result.append((curr_start, curr_end))

    return result

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED!\n"

"""Bonus Qs:
    1. What if we did have an upper bound on the input values? Could we improve our runtime? Would it cost us memory?
    2. Could we do this "in-place" on the input list and save some space? What are the pros and cons of doing this in-place?
"""
