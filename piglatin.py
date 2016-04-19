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

def pig_latin(phrase):
    """Turn a phrase into pig latin.

    There will be no uppercase letters or punctuation in the phrase.

        >>> pig_latin('hello awesome programmer')
        'ellohay awesomeyay rogrammerpay'
    """

    # COULD REFACTOR, USE LIST COMPREHENSION
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

# print pig_latin('hello awesome programmer')

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. REATGAY OBJAY!\n"
