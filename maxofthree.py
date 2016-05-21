"""Find the largest of three numbers.

Define a function max_of_three() that takes in three numbers as arguments and
returns the largest of them. Do not use the built in 'max' method.

For example::

    >>> max_of_three(1, 3, 2)
    3

    >>> max_of_three(5, 5, 5)
    5

    >>> max_of_three(10, 2, 11)
    11

    >>> max_of_three(5, 5, 10)
    10

"""

# Solution 1
def max_of_three(num1, num2, num3):
    """Returns the largest of three integers"""

    max_num = num1
    if num2 > max_num:
        max_num = num2
    if num3 > max_num:
        max_num = num3

    return max_num


# Solution 2
def max_of_three(num1, num2, num3):
    """Returns the largest of three integers"""

    return max(num1, num2, num3)


# Solution 3
def max_of_three(num1, num2, num3):
    """Returns the largest of three integers"""

    if num1 > num2:
        largest = num1
    else:
        largest = num2

    if num3 > largest:
        largest = num3

    return largest


# Solution 4 (HB)
def max_of_three(num1, num2, num3):
    """Returns the largest of three integers"""

    if num1 >= num2 and num1 >= num3:
        return num1

    elif num2 >= num1 and num2 >= num3:
        return num2

    elif num3 >= num2 and num3 >= num1:
        return num3

    else:
        return "Something went wrong"

if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. MAXIMALLY EXCELLENT!\n"
