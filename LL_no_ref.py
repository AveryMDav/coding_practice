class node(object):

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"<Node Object. Data: {self.data}; Next: {self.next.data if self.next else None}>"


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        return f"<Linked List. Head:{self.head if self.head else None}; Tail:{self.tail.data if self.tail else None}"

    def append(self, data):
        """add a new node to end of list"""

        new_node = node(data)

        if self.head is None:
            self.head = new_node

        if self.tail is not None:
            self.tail.next = new_node

        self.tail = new_node

    def insert(self, data):
        """add a new node to start of list"""

        new_node = node(data)

        if self.head is None:
            self.head = new_node

        if self.head is not None:
            old = self.head
            self.head = new_node
            self.head.next = old

    def print_list(self):
        """print out every item in list"""

        while self.head is not None:
            print(self.head.data)
            self.head = self.head.next

    def remove(self, data):
        """removes specified item from list"""

        while self.head is not None:
            if self.head.data == data:
                self.head = self.head.next
                if self.head is None:
                    self.tail = None
                return
            else:




ll = LinkedList()
ll.append("apple")
ll.append("orange")
ll.insert("grape")
ll.print_list()
