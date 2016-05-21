"""Turn a phrase into Pig Latin.

This takes a space-separated phrase and returns it in Pig Latin.

Rules:

1. If the word begins with a consonant (not a, e, i, o, u),
   move the first letter to the end and add 'ay'

2. If the word begins with a vowel, add 'yay' to the end

For example:

    >>> pig_latin('hello awesome programmer')
    'ellohay awesomeyay rogrammerpay'

"""
# # Solution 1
def pig_latin(phrase):
    """Turn a phrase into pig latin.

    There will be no uppercase letters or punctuation in the phrase.

        >>> pig_latin('hello awesome programmer')
        'ellohay awesomeyay rogrammerpay'
    """

    # split phrase into words
    # for each word, get the first letter
    # if the first letter is a consonant:
    #   remove first letter, and add first letter + 'ay' to end of current word
    # If the first letter is a vowel:
    #   add 'yay' to the end of the word

    vowels = {'a', 'e', 'i', 'o', 'u'}
    words = phrase.split(" ")
    result = []

    for word in words:
        if word[0] in vowels:
            result.append(word + 'yay')
        else:
            result.append(word[1:] + word[0] + 'ay')

    return " ".join(result)

# HB Solution
# Solution 2: Using list comprehension and helper method
def pig_latin_word(word):
    """Convert word to pig latin

        For example::

        >>> pig_latin_word('porcupine')
        'orcupinepay'

        >>> pig_latin_word('apple')
        'appleyay'
    """

    if word[0] in 'aeiou':
        return word + "yay"
    else:
        return word[1:] + word[0] + "ay"


def pig_latin(phrase):
    """Turn a phrase into pig latin.

    There will be no uppercase letters or punctuation in the phrase.

        >>> pig_latin('hello awesome programmer')
        'ellohay awesomeyay rogrammerpay'
    """

    words = phrase.split(" ")

    pl_words = [pig_latin_word(word) for word in words]

    return " ".join(pl_words)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. REATGAY OBJAY!\n"
