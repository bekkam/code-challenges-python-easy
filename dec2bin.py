"""Convert a decimal number to binary representation.

For example::

    >>> dec2bin_backwards(0)
    '0'

    >>> dec2bin_backwards(1)
    '1'

    >>> dec2bin_backwards(2)
    '10'

    >>> dec2bin_backwards(4)
    '100'

    >>> dec2bin_backwards(15)
    '1111'

For example, using our alternate solution::

    >>> dec2bin_forwards(0)
    '0'

    >>> dec2bin_forwards(1)
    '1'

    >>> dec2bin_forwards(2)
    '10'

    >>> dec2bin_forwards(4)
    '100'

    >>> dec2bin_forwards(15)
    '1111'

"""

# Solution 1: convert decimal to binary using a stack
class Stack(object):

    def __init__(self):
        self._stack = []

    def push(self, item):
        """Push item onto to top of stack"""

        self._stack.append(item)

    def pop(self):
        """Remove top item of stack"""

        return self._stack.pop()

    def peek(self):
        """Return, but don't remove, top item of stack"""

        return self._stack[-1]

    def is_empty(self):
        """Return true if stack is empty, else return false"""

        return not self._stack


def dec2bin(num):
    """Convert a decimal number to binary representation."""

    result = ""
    stack = Stack()

    # if the remainder of num/2 is even, push 0 to stack. otherwise, push 1 to stack.
    # num = num/2
    while num >= 1:
        remainder = num % 2
        stack.push(0) if remainder % 2 == 0 else stack.push(1)
        num = num/2

    while stack.is_empty() is False:
        result += str(stack.pop())

    return result

# print dec2bin(15)

# ##############################################################
# Solution 2
def dec2bin_forwards(num):
    """Convert decimal to binary by first calculating the number of bits(places)"""

    out = ""

    # Figure out how many bits(place-values) this will have
    num_bits = 1

    while 2 ** num_bits <= num:
        print num_bits
        num_bits += 1

    """For every place value, starting with the highest place-value:
        subtract [2 to the exponent of place-value] from num.
        If the result is greater than 0, add 1 to out. Else add 0 to out
    """
    for position in range(num_bits - 1, -1, -1):
        print "num is ", num
        print "position is ", position
        if 2 ** position <= num:
            num -= 2 ** position
            out += "1"
            print "added 1 to out"

        else:
            print "added 0 to out"
            out += "0"
        print "out is ", out

    return out

print dec2bin_forwards(5)



# if __name__ == '__main__':
#     import doctest
#     if doctest.testmod().failed == 0:
#         print "\n*** ALL TEST PASSED. W00T!\n"
