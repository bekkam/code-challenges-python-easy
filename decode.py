"""Decode a string.

A valid code is a sequence of numbers and letter, always starting with a number
and ending with letter(s).

Each number tells you how many characters to skip before finding a good letter.
After each good letter should come the next next number.

For example, the string "hey" could be encoded by "0h1ae2bcy". This means
"skip 0, find the 'h', skip 1, find the 'e', skip 2, find the 'y'".

A single letter should work::

    >>> decode("0h")
    'h'

    >>> decode("2abh")
    'h'

Longer patterns should work::

    >>> decode("0h1ae2bcy")
    'hey'
"""

# 3.19227981567
def decode(s):
    """Decode a string."""

    # START SOLUTION

    word = ""

    i = 0

    while i < len(s):

        num_to_skip = int(s[i])
        i += num_to_skip + 1

        word += s[i]

        i += 1

    return word

if __name__ == '__main__':
    import doctest
    import timeit

    print(timeit.timeit("decode('0h1ae2bcy')",
                        setup="from __main__ import decode"))
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; 0G1ar0e1ba0t2ab! ***\n"
