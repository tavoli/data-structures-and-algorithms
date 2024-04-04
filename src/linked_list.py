class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_head(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        if not self.tail:
            self.tail = node
    
    def insert_tail(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def remove(self, index):
        if index < 0 or not self.head:
            return False
        if index == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            return True

        prev = None
        current = self.head
        count = 0
        while current and count != index:
            prev = current
            current = current.next
            count += 1
        if not current:
            return False
        if current == self.tail:
            self.tail = prev
        prev.next = current.next
        return True
    
    def get(self, index):
        if index < 0 or not self.head:
            return -1
        count = 0
        current = self.head
        while current and count != index:
            current = current.next
            count += 1
        if not current:
            return -1
        return current.data
    
    def get_values(self):
        res = []
        current = self.head
        while current:
            res.append(current.data)
            current = current.next
        return res

