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

# Solution 1 (HB)
# Runtime: O(N)
# uses a boolean rather than a list, bc as soon as number of odds > 1, can return false
# 4.15115785599
def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""

    """To use less space, rather than adding odd-numbered letters to a new list,
    we bind identifier seen_an_odd to boolean False.  We set it to True as soon
    as a letter count in seen is an odd value.  If seen_an_odd is True, we
    return False, because it means that there is more than one letter in word
    that has an odd count"""

    seen = {}
    # It's a palindrome if the number of odd-counts is either 0 or 1
    # create a dictionary of letter counts

    for letter in word:
        count = seen.get(letter, 0)
        seen[letter] = count + 1

    # Return False if more than 1 letter has an odd count
    seen_an_odd = False

    for count in seen.values():
        if count % 2 != 0:
            if seen_an_odd:
                return False
            seen_an_odd = True

    return True


# Solution 2
# stores odd counts in a list (slower)
# 4.88915300369
def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""

    letter_counts = {}

    for letter in word:
        count = letter_counts.get(letter, 0)
        letter_counts[letter] = count + 1

    odds = []
    for count in letter_counts.values():
        if count % 2 != 0:
            if not odds:
                odds.append(count)
            else:
                return False
    return True


# Solution 3
# Uses list, as well as setdefault (slowest)
# 4.84743118286
def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""

    seen = {}

    # create a dictionary of letter counts
    for letter in word:
        seen.setdefault(letter, 0)
        seen[letter] = seen[letter] + 1

    odds = []

    for val in seen.values():
        if val % 2 == 1:
            if odds:
                return False
            odds.append(val)
    return True

if __name__ == '__main__':
    import doctest
    import timeit

    print(timeit.timeit("is_anagram_of_palindrome('arceaceb')",
             setup="from __main__ import is_anagram_of_palindrome"))

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. AWESOMESAUCE!\n"
