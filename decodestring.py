"""In this challenge, you’ll write a decoder.

A valid code is a sequence of numbers and letters, always starting with
a number and ending with letter(s).

Each number tells you how many characters to skip before finding a good letter.
After each good letter should come the next next number.

For example, the string “hey” could be encoded by “0h1ae2bcy”. 
This means “skip 0, find the ‘h’, skip 1, find the ‘e’, skip 2, find the ‘y’”.

A single letter should work:

>>> decode("0h")
'h'

>>> decode("2abh")
'h'

Longer patterns should work:

>>> decode("0h1ae2bcy")
'hey'

We’ve provided a file, decode.py, with a stub function in it:"""

def decode(encoded_string):
    """Decode a string."""

    """

    result = ""

    for each item in the string:
        if item is a number:
            if item is 0:
                add the next item to the result string
            if item is > 0:
                "skip" that many items in the string, to get to the next letter to
                add to result"""

    result = ""

    i = 0
    while i < len(encoded_string):
        current = encoded_string[i]
        # find each number
        if current.isalpha() is False:
            if current == 0:
                result += encoded_string[i + 1]
            else:
                result += encoded_string[i + current + 1]

        i += 1

    return result

print decode("0h1ae2bcy")
