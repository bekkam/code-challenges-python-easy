"""Print points in matrix, going in a spiral.

Give a square matrix, like this 4 x 4 matrix, it's composed
of points that are x, y points (top-left is 0, 0):

    0,0  1,0  2,0  3,0
    0,1  1,1  2,1  3,1
    0,2  1,2  2,2  3,2
    0,3  1,3  2,3  3,3

Starting at the top left, print the x and y coordinates of each
point, continuing in a spiral.

(Since we provide 3 different versions, you can change this to
the routine you want to test:

    >>> spiral = spiral_by_nested_boxes

Here are different sizes:

    >>> spiral(1)
    (0, 0)

    >>> spiral(2)
    (0, 0)
    (1, 0)
    (1, 1)
    (0, 1)

    >>> spiral(3)
    (0, 0)
    (1, 0)
    (2, 0)
    (2, 1)
    (2, 2)
    (1, 2)
    (0, 2)
    (0, 1)
    (1, 1)

    >>> spiral(4)
    (0, 0)
    (1, 0)
    (2, 0)
    (3, 0)
    (3, 1)
    (3, 2)
    (3, 3)
    (2, 3)
    (1, 3)
    (0, 3)
    (0, 2)
    (0, 1)
    (1, 1)
    (2, 1)
    (2, 2)
    (1, 2)
"""


def spiral(matrix_size):
    """Spiral coordinates of a matrix of `matrix_size` size."""
    """
    y = num of items in list
    x = num of items in nested list
    """
    if matrix_size < 2:
        return "Insufficient size to create matrix"

    result = []
    top = 0
    right = matrix_size - 1
    down = matrix_size - 1
    left = 0

    while True:
        # add top row
        i = left
        while i <= right:
            result.append((top, i))
            i += 1
        top += 1

        if(top > down or left > right):
            break

        # add right most column
        j = top
        while j <= down:
            result.append((j, right))
            j += 1
        right -= 1

        if(top > down or left > right):
            break

        # add bottom row
        i = right
        while i >= left:
            result.append((down, i))
            i -= 1
        down -= 1

        if(top > down or left > right):
            break

        # add left most column
        j = down
        while j >= top:
            result.append((j, left))
            j -= 1
        left += 1
        if(top > down or left > right):
            break

    return result

# print spiral(4)


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU MUST BE DIZZY WITH PRIDE!\n"
