"""Is this word a palindrome?

    >>> is_palindrome("a")
    True

    >>> is_palindrome("noon")
    True

    >>> is_palindrome("racecar")
    True

    >>> is_palindrome("porcupine")
    False

Treat spaces and uppercase letters normally:

    >>> is_palindrome("Racecar")
    False
"""


def is_palindrome(word):
    """Return True/False if this word is a palindrome."""

    mid = (len(word))/2

    # for each letter in word upto middle, if the first == last, its a palindrome

    for i in range(0, mid):
        if word[i] != word[-(i + 1)]:
            return False

    return True


# print is_palindrome("test")


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YAY!"
