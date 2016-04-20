"""Is the tree at this node balanced?

To make this a bit more readable, let's alias our class name:

    >>> N = BinaryNode

For a tree of 1 item:

    >>> tree1 = N(1)
    >>> tree1.is_balanced_nonrecursive()
    True

For a tree of 2 items:

  1
 /
2

    >>> tree2 = N(1,
    ...           N(2))
    >>> tree2.is_balanced_nonrecursive()
    True

Three:

  1
 / \
2   3

    >>> tree3 = N(1,
    ...           N(2), N(3))
    >>> tree3.is_balanced_nonrecursive()
    True

Four:

     1
    / \
   2   4
  /
 3

    >>> tree4 = N(1,
    ...           N(2,
    ...             N(3)),
    ...           N(4))
    >>> tree4.is_balanced_nonrecursive()
    True

Five:

     1
   /---\
  2     5
 / \
3   4

    >>> tree5 = N(1,
    ...           N(2,
    ...             N(3), N(4)),
    ...           N(5))
    >>> tree5.is_balanced_nonrecursive()
    True

Imbalanced Four:

    1
   /
  2
 / \
3   4

    >>> tree4i = N(1,
    ...            N(2,
    ...              N(3), N(4)))
    >>> tree4i.is_balanced_nonrecursive()
    False
"""


class BinaryNode(object):
    """Node in a binary tree."""

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def is_balanced_nonrecursive(self):
        """Is the tree at this node balanced?"""

        # tree is not balanced if:
        # a node has only one child, and that child has children???
        to_visit = [self]
        while to_visit:
            node = to_visit.pop()
                # check if that child has 2 children
                # if there are 2 children, return False
                # else: continue
            if node.left and not node.right:
                if node.left.left and node.left.right:
                    return False
            if node.right and not node.left:
                if node.right.left and node.right.right:
                    return False
            # add left and right, if they are not none
            if node.right:
                to_visit.append(node.right)
            if node.left:
                to_visit.append(node.left)

        return True


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED! GO GO GO!\n"
