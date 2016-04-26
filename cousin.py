"""Find 'cousin' nodes -- those nodes at the same level as a node.

Consider the tree::

            a
        ---------
       /    |    \
      b     c     d
     /-\   /-\   /-\
    e  f  g  h  i  j
        \     \
        k     l

Nodes `k` and `l` are at same level ("cousins", a we'll call them, but removed
by several levels). Similarly `e`, `f`, `g`, `h`, `i`, and `j` are cousins, as are
`b`, `c`, and `d`.

Let's create this tree::

    >>> a = Node("a")

    >>> b = Node("b")
    >>> c = Node("c")
    >>> d = Node("d")
    >>> b.set_parent(a)
    >>> c.set_parent(a)
    >>> d.set_parent(a)

    >>> e = Node("e")
    >>> f = Node("f")
    >>> g = Node("g")
    >>> h = Node("h")
    >>> i = Node("i")
    >>> j = Node("j")
    >>> e.set_parent(b)
    >>> f.set_parent(b)
    >>> g.set_parent(c)
    >>> h.set_parent(c)
    >>> i.set_parent(d)
    >>> j.set_parent(d)

    >>> k = Node("k")
    >>> l = Node("l")
    >>> k.set_parent(f)
    >>> l.set_parent(h)

Let's find the cousins for b::

    >>> b.cousins() == {c, d}
    True

    >>> c.cousins() == {b, d}
    True

    >>> e.cousins() == {f, g, h, i, j}
    True

    >>> k.cousins() == {l}
    True

The root node has no cousins::

    >>> a.cousins() == set()
    True
"""


class Node(object):
    """Doubly-linked node in a tree.

        >>> na = Node("na")
        >>> nb1 = Node("nb1")
        >>> nb2 = Node("nb2")

        >>> nb1.set_parent(na)
        >>> nb2.set_parent(na)

        >>> na.children
        [<Node nb1>, <Node nb2>]

        >>> nb1.parent
        <Node na>
    """

    parent = None

    def __init__(self, data):
        self.children = []
        self.data = data

    def __repr__(self):
        return "<Node %s>" % self.data

    def set_parent(self, parent):
        """Set parent of this node.

        Also sets the children of the parent to include this node.
        """

        self.parent = parent
        parent.children.append(self)


# Solution 1: Recursive solution
    def cousins(self):
        """Find nodes on the same level as this node."""

        current = self
        # Get level of this node
        level = 0
        while current.parent is not None:
            level += 1
            current = current.parent

        cousins = set()
        # recursive function to find a node, examine its children, and decide
        # whether to add it to set of cousins
        def _get_cousins(node, current_depth):

            # base case: this is a leaf node, so can't recurse further down
            if node is None:
                return
            # base case: we are at the desired level
            if current_depth == level:
                cousins.add(node)
                return
            # if we aren't at desired level or at a leaf node, call this function
            # on the current node's children
            for child in node.children:
                # print "cousins is ", cousins
                _get_cousins(child, current_depth + 1)

        _get_cousins(current, 0)

        # return all cousins, removing self first
        cousins.remove(self)
        return cousins

# HB Solution
    # def cousins(self):
    #     """Find nodes on the same level as this node."""

    #     # START SOLUTION

    #     # Find our depth (0=root node, 1=child-of-root, etc)
    #     # and the root of the tree. We'll do this by walking up the tree
    #     # until we find the root, counting our steps up.

    #     current = self
    #     sought_depth = 0

    #     while current.parent is not None:
    #         sought_depth += 1
    #         current = current.parent

    #     # Now, "current" is the root node, as we navigated to the top
    #     #
    #     # Now, let's navigate back down to that level. We'll do this
    #     # recursively, but we could do it with a stack, too.

    #     # Set of cousins we'll find.
    #     #
    #     # Sets are mutable, so we'll just mutate this copy in place as
    #     # we find cousins.

    #     cousins = set()

    #     # Recursive function to find examine a node, decide whether to
    #     # consider it a cousin, and to explore its children.
    #     #
    #     # We could make this a free-standing function outside of the class,
    #     # of a method of the class -- but we don't need access to the
    #     # `self`, and by nesting this, we'll have access to the
    #     # `cousins` and `sought_depth` variables, so we conveniently don't
    #     # need to pass them around explicitly.

    #     def _cousins(node, curr_depth):

    #         # Base case: we're a leaf node, so can't look further
    #         if node is None:
    #             return

    #         # Second base case: we're at the right level, so don't need
    #         # to look further
    #         if curr_depth == sought_depth:
    #             cousins.add(node)
    #             return

    #         for child in node.children:
    #             # Look at the children, noting that we're one level deeper then.
    #             _cousins(child, curr_depth + 1)

    #     _cousins(node=current, curr_depth=0)

    #     # We don't want to include the original node
    #     cousins.remove(self)
    #     return cousins

# Solution 0: (iterative solution, misses a test case)
    # def cousins(self):
    #     """Find nodes on the same level as this node."""

    #     # get parent of this node
    #     # get all kids of parent
    #     # get all siblings of parent
    #     # get all parent's siblings' kids
    #     result = set()
    #     # if we are at root
    #     if self.parent is None:
    #         return set()
    #     elif self.parent:
    #         if self.parent.parent is None:
    #             for child in self.parent.children:
    #                 if child != self:
    #                     result.add(child)
    #         else:
    #             parent = self.parent
    #             grandparent = self.parent.parent
    #             all_parents = grandparent.children
    #             # print "all_parents is ", all_parents
    #             for parent in all_parents:
    #                 for child in parent.children:
    #                     if child != self:
    #                         result.add(child)
    #         return set(result)

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; GREAT JOB! ***\n"
