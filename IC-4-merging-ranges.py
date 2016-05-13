def condense_meeting_times1(list_of_tuples_of_meeting_times):
    """Takes a list of meeting time ranges and returns condensed list of ranges
    for all meetings.

    Given an unordered list of tuples that represent ranges, return a list of
    tuples representing all non-overlapping ranges.  For example, given:

        [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

    your function would return:

        [(0, 1), (3, 8), (9, 12)]


    Here's a formal algorithm:

    1. We treat the meeting with earlier start time as "first," and the other as "second."
    2. If the end time of the first meeting is equal to or greater than the start
    time of the second meeting, we merge the two meetings into one time range.
    The resulting time range's start time is the first meeting's start, and its
    end time is the later of the two meetings' end times.
    3. Else, we leave them separate.

    >>> condense_meeting_times1([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
    [(0, 1), (3, 8), (9, 12)]

    >>> condense_meeting_times1([(1, 5), (2, 3)])
    [(1, 5)]

    >>> condense_meeting_times1([(1, 10), (2, 6), (3, 5), (7, 9)])
    [(1, 10)]
    """

    list_of_tuples_of_meeting_times.sort()

    # initialize counters to 1 below normal, so that counters are incremented
    # at beginning of loop.  This way, we don't have to increment counters within
    # every case in the while-loop (which uses continue)
    i = -1
    j = 0
    result = []

    while j < len(list_of_tuples_of_meeting_times):
        i += 1
        j += 1

        # Case 1:
        # if both the start and end of first is within range of most recently
        # added tuple to result, skip to next tuple in the list
        if len(result) >= 1:
            last_added = result[-1]
            if list_of_tuples_of_meeting_times[i][1] <= last_added[1]:
            # skip to next iteration
                continue

        # Case 2:
        # if first end >= 2nd start - that is, first meeting ends after 2nd
        # meeting starts - then the 2nd meeting either ends later than the 1st
        # meeting ends, or it doesnt.
        if list_of_tuples_of_meeting_times[i][1] >= list_of_tuples_of_meeting_times[j][0]:
            # if 1st end >= 2nd end - that is, if first meeting ends the same
            # time or after the 2nd meeting ends - then add the first meetings
            # start and end times to result
            start = list_of_tuples_of_meeting_times[i][0]
            if list_of_tuples_of_meeting_times[i][1] >= list_of_tuples_of_meeting_times[j][1]:
                stop = list_of_tuples_of_meeting_times[i][1]
            # otherwise, add the first meeting's start, and the 2nd meeting's
            # end to result
            else:
                stop = list_of_tuples_of_meeting_times[j][1]
            result.append((start, stop))
            # increment counters and skip to next iteration
            continue

        # Case 3:
        # if the first meeting ends before the start of the 2nd meeting, add
        # first meeting to result, and continue to next iteration
        else:
            result.append(list_of_tuples_of_meeting_times[i])
    return result

# print condense_meeting_times1([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
# print condense_meeting_times1([(1, 5), (2, 3)])
# print condense_meeting_times1([(1, 10), (2, 6), (3, 5), (7, 9)])


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED!\n"
