"""Given a list, sort it using insertion sort.

For example::

    >>> from random import shuffle
    >>> alist = range(1, 11)

    >>> shuffle(alist)
    >>> insertion_sort(alist)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    >>> shuffle(alist)
    >>> insertion_sort(alist)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    >>> shuffle(alist)
    >>> insertion_sort(alist)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""


# Runtime: )(N^2)
def insertion_sort(alist):
    """Given a list, sort it using insertion sort."""

    """Insertion Sort:
    if item 2 < item 1. swap.
    if item 3 < item 2. swap
        if item 2 < item 1. swap.
    """

    i = 1

    while i < len(alist):
        # store value of current element as current
        current = alist[i]
        # create a variable that will store the location to place the element
        location = i
        # *********** run this loop if our current item is less than the item before it ****************
        while location > 0 and alist[location - 1] > current:
            # replace alist[location] with the item before it
            alist[location] = alist[location - 1]
            # decrement location
            location -= 1
        # when our current item is not less than the item before it, insert
        # item at location
        alist[location] = current
        # get the next item in the list
        i += 1
    return alist

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. NICE SORTING!\n"
