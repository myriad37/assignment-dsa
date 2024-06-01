class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Inserting a Node at Any Given Position in a Singly Linked List
    def insert_node(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        for i in range(position - 1):
            if current is None:
                return
            current = current.next

        new_node.next = current.next
        current.next = new_node

    # 2. Deleting a Node at Any Given Position in a Singly Linked List
    def delete_node(self, position):
        if self.head is None:
            return

        if position == 0:
            self.head = self.head.next
            return

        current = self.head
        for i in range(position - 1):
            if current is None or current.next is None:
                return
            current = current.next

        if current.next is None:
            return

        current.next = current.next.next

    # 3. Deleting a Node After a Given Node in a Singly Linked List
    def delete_after_node(self, node_data):
        if self.head is None:
            return

        current = self.head
        while current.data != node_data:
            if current.next is None:
                return
            current = current.next

        if current.next is None:
            return

        current.next = current.next.next

    # 4. Searching a Node in a Singly Linked List
    def search_node(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False

    # 5. Implementing a Stack Using Linked Lists
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            return None

        data = self.head.data
        self.head = self.head.next
        return data

    def peek(self):
        if self.head is None:
            return None
        return self.head.data