class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"<Node object. Data: {self.data}; Next: {self.next.data if self.next else None}>"


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        return f"<Linked List. Head: {self.head if self.head else None}; Tail: {self.tail.data if self.head else None}>"

    def append(self, data):
        """append node with data to the end of list"""

        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        if self.tail is not None:
            self.tail.next = new_node

        self.tail = new_node


