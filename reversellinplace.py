"""Given linked list, reverse the nodes in this linked list in place.

For example:

    >>> ll = LinkedList(Node(1, Node(2, Node(3))))
    >>> reverse_linked_list_in_place(ll)
    >>> ll.as_string()
    '321'

"""


class LinkedList(object):
    """Linked list."""

    def __init__(self, head=None):
        self.head = head

    def as_string(self):
        """Represent data for this list as a string.

        >>> LinkedList(Node(3)).as_string()
        '3'

        >>> LinkedList(Node(3, Node(2, Node(1)))).as_string()
        '321'
        """

        out = []
        n = self.head

        while n:
            out.append(str(n.data))
            n = n.next

        return "".join(out)


class Node(object):
    """Class in a linked list."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def reverse_linked_list_in_place(lst):
    """Given linked list, reverse the nodes in this linked list in place."""

    current = lst.head
    prev = None

    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    # return prev


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. RIGHT ON!\n"


# lst = [0, 1, 2, 3, 4]

# prev = None
# i = 0
# current = lst[i]
# while current is not None:
#     next = lst[i + 1]
#     print "next is ", next
#     lst[i + 1] = prev
#     print "curr.next is ", prev
#     prev = lst[i]
#     print "prev is ", prev
#     current = lst[i + 1]
#     print "current is ", current
#     i += 1

# lst[0] = prev

# print lst


