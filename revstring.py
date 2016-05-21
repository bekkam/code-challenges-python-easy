"""Reverse a string.

For example::

    >>> rev_string("")
    ''

    >>> rev_string("a")
    'a'

    >>> rev_string("porcupine")
    'enipucrop'

"""


# Solution 1
def rev_string1(astring):
    """Return reverse of string.

    You may NOT use the reversed() function!
    """

    result = ""

    for letter in astring:
        result = letter + result

    return result

# Solution 2 (HB solution)
def rev_string2(astring):
    """Return reverse of string.

    You may NOT use the reversed() function!
    """

    out = ""

    for i in range(len(astring), 0, -1):
        out += astring[i - 1]

    return out


if __name__ == '__main__':
    import doctest
    import timeit

    time1 = (timeit.timeit("rev_string1('hello')",
             setup="from __main__ import rev_string1"))

    time2 = (timeit.timeit("rev_string2('hello')",
             setup="from __main__ import rev_string2"))

    print "Timer results for Solution 1: ", time1           # 1.06165504456
    print "Timer results for Solution 2: ", time2           # 1.75967407227

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. !KROW DOOG\n"
