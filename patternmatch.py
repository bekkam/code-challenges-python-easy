"""Check if pattern matches.

Given a "pattern string" starting with "a" and including only "a" and "b"
characters, check to see if a provided string matches that pattern.

For example, the pattern "aaba" matches the string "foofoogofoo" but not
"foofoofoodog".

Patterns can only contain a and b and must start with a:

    >>> pattern_match("b", "foo")
    Traceback (most recent call last):
    ...
    AssertionError: invalid pattern

    >>> pattern_match("A", "foo")
    Traceback (most recent call last):
    ...
    AssertionError: invalid pattern

    >>> pattern_match("abc", "foo")
    Traceback (most recent call last):
    ...
    AssertionError: invalid pattern

The pattern can contain only a's:

    >>> pattern_match("a", "foo")
    True

    >>> pattern_match("aa", "foofoo")
    True

    >>> pattern_match("aa", "foobar")
    False

It's possible for a to be zero-length (a='', b='hi'):

    >>> pattern_match("abbab", "hihihi")
    True

Or b to be zero-length (a='foo', b=''):

    >>> pattern_match("aaba", "foofoofoo")
    True

Or even for a and b both to be zero-length (a='', b=''):

    >>> pattern_match("abab", "")
    True

But, more typically, both are non-zero length:

    >>> pattern_match("aa", "foodog")
    False

    >>> pattern_match("aaba" ,"foofoobarfoo")
    True

    >>> pattern_match("ababab", "foobarfoobarfoobar")
    True

Tricky: (a='foo', b='foobar'):

    >>> pattern_match("aba" ,"foofoobarfoo")
    True
"""


def pattern_match(pattern, astring):
    """Can we make this pattern match this string?"""

    # Q&D sanity check on pattern
    assert (pattern.replace("a", "").replace("b", "") == ""
            and pattern.startswith("a")), "invalid pattern"

    count_a = pattern.count('a')
    count_b = pattern.count('b')

    # for all possible lengths of a (including if length of b is 0)
    for length_a in range(0, len(astring)/count_a + 1):
        # calculate how long b would be for a given length of a:
        if count_b:
            length_b = (len(astring) - (length_a * count_a))/count_b
        else:
            length_b = 0

        # create a test string with our current values for a and b
        test = ""
        a = astring[0:length_a]
        b = astring[length_a:length_a + length_b]

        for letter in pattern:
            if letter == 'a':
                test += a
            if letter == 'b':
                test += b
        # return true if our test string matches astring
        if test == astring:
            return True

    return False


# Solution 2 (HB)
def pattern_match(pattern, astring):
    """Can we make this pattern match this string?"""

    # Q&D sanity check on pattern

    assert (pattern.replace("a", "").replace("b", "") == ""
            and pattern.startswith("a")), "invalid pattern"

    # START SOLUTION

    count_a = pattern.count("a")  # num times a appears in pattern
    count_b = pattern.count("b")  # num times b appears in pattern
    first_b = pattern.find("b")  # index of first b (-1 if not in pattern)

    # We'll check every possible length of a, from 0 to the max
    # (where the max is affected by the count of how many a's must appear)

    for a_length in range(0, len(astring) / count_a + 1):

        # For this length of a, find required length of b
        if count_b:
            b_length = (len(astring) - (a_length * count_a)) / float(count_b)
        else:
            b_length = 0

        # Fast fail optimization: b_length must be int and >= 0
        if int(b_length) != b_length or b_length < 0:
            continue

        # Find where b would need to begin
        b_start = first_b * a_length

        # Check if this is a workable match; if so, we win!
        if matches(pattern=pattern,
                   a=astring[0:a_length],
                   b=astring[b_start:b_start + int(b_length)],
                   astring=astring):
            return True

    return False

if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. WE'RE WELL-MATCHED!\n"
