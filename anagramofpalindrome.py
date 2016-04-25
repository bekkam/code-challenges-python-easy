"""Is the word an anagram of a palindrome?

A palindrome is a word that reads the same forward and backwards
(eg, "racecar", "tacocat"). An anagram is a rescrambling of a word
(eg for "racecar", you could rescramble this as "arceace").

Determine if the given word is a re-scrambling of a palindrome.
The word will only contain lowercase letters, a-z.

Examples::

    >>> is_anagram_of_palindrome("a")
    True

    >>> is_anagram_of_palindrome("ab")
    False

    >>> is_anagram_of_palindrome("aab")
    True

    >>> is_anagram_of_palindrome("arceace")
    True

    >>> is_anagram_of_palindrome("arceaceb")
    False

"""

# Solution 1: O(N)
def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""

    if len(word) == 1:
        return True

    seen = {}

    # create a dictionary of letter counts
    for letter in word:
        seen.setdefault(letter, 0)
        seen[letter] = seen[letter] + 1

    odds = []

    for val in seen.values():
        if val % 2 == 1:
            odds.append(val)

    return False if len(odds) > 1 else True


# Solution 2
def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""

    """To use less space, rather than adding odd-numbered letters to a new list,
    we bind identifier seen_an_odd to boolean False.  We set it to True as soon
    as a letter count in seen is an odd value.  If seen_an_odd is True, we
    return False, because it means that there is more than one letter in word
    that has an odd count"""

    seen = {}

    # create a dictionary of letter counts
    for letter in word:
        seen.setdefault(letter, 0)
        seen[letter] = seen[letter] + 1

    # return False if more than 1 letter has an odd count
    seen_an_odd = False

    for val in seen.values():
        if val % 2 == 1:
            if seen_an_odd:
                return False
            seen_an_odd = True

    return True


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. AWESOMESAUCE!\n"
