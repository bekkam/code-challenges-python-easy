"""Split astring by splitter and return list of splits.

This should work like that built-in Python .split() method [*].
YOU MAY NOT USE the .split() method in your solution!
YOU MAY NOT USE regular expressions in your solution!

For example:

    >>> split("i love balloonicorn", " ")
    ['i', 'love', 'balloonicorn']

    >>> split("that is which is that which is that", " that ")
    ['that is which is', 'which is that']

    >>> split("that is which is that which is that", "that")
    ['', ' is which is ', ' which is ', '']

    >>> split("hello world", "nope")
    ['hello world']

* Note: the actual Python split method has special behavior
  when it is not passed anything for the splitter -- you do
  not need to implemented that.

"""


def split(astring, splitter):
    """Split astring by splitter and return list of splits."""

    result_list = []

    splitter_length = len(splitter)

    # iterate over each character in the string
    # current segement = astring[end:i+j]
    # if current segment = splitter, slice from beginning up to but not including
    # i, and add it to result_list
    # increment i
    # when finish looping, add remaining segment to result_list

    i = 0
    j = len(splitter)
    end = 0
    while (i + j <= len(astring)):
        current_segment = astring[i: i + j]
        if current_segment == splitter:
            # slice from beginning up to but not including i
            result_list.append(astring[end:i])
            end = i + j
        i += 1
    # append last segment after splitter (or entire segment if no splitter)
    result_list.append(astring[end:])

    return result_list




# print split("i love balloonicorn", " ")




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. FINE SPLITTING!\n"
