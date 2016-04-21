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

    >>> spiral = spiral_recursion

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

# Unfinished solution: Prints clockwise spiral, starting at top right corner
# def spiral(matrix_size):
#     """Spiral coordinates of a matrix of `matrix_size` size."""
#     """
#     y = num of items in list
#     x = num of items in nested list
#     """
#     if matrix_size < 2:
#         return "Insufficient size to create matrix"

#     result = []
#     top = 0
#     right = matrix_size - 1
#     down = matrix_size - 1
#     left = 0

#     while True:
#         # add top row
#         i = left
#         while i <= right:
#             result.append((top, i))
#             i += 1
#         top += 1

#         if(top > down or left > right):
#             break

#         # add right most column
#         j = top
#         while j <= down:
#             result.append((j, right))
#             j += 1
#         right -= 1

#         if(top > down or left > right):
#             break

#         # add bottom row
#         i = right
#         while i >= left:
#             result.append((down, i))
#             i -= 1
#         down -= 1

#         if(top > down or left > right):
#             break

#         # add left most column
#         j = down
#         while j >= top:
#             result.append((j, left))
#             j -= 1
#         left += 1
#         if(top > down or left > right):
#             break

#     return result


def spiral_recursion(matrix_size):
    """Spiral matrix of `matrix_size` size.

    This version works by drawing TRBL boxes until the entire matrix
    has been printed. Rather than a loop, it uses recursion.
    """

    def spiral_inner(box_number):

        # top and left refer to the starting index of x and y respectively
        top = left = box_number
        # bottom and right refer to the max index of x and y respectively
        bottom = right = matrix_size - box_number - 1

        # create a base case that will terminate recursion:
        if box_number == matrix_size/2:
            # if its odd, print center
            if matrix_size % 2 == 1:
                print (matrix_size/2, matrix_size/2)

            return

        # print top row
        for x in range(left, right):
            print (x, top)
            # prints: 00, 10, 20, 30

        # print right column
        for y in range(top, bottom):
            print (right, y)

        # print bottom
        for x in range(right, left, -1):
            print (x, bottom)

        # print left
        for y in range(bottom, top, -1):
            print (left, y)

        spiral_inner(box_number + 1)

    spiral_inner(0)


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU MUST BE DIZZY WITH PRIDE!\n"
