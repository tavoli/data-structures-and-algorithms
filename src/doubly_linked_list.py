class Node:
    def __init__(self, val = 0, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def get(self, index: int) -> int:
        if index >= self.size:
            return
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return

        node = Node(val)
        if index == 0:
            if self.size:
                node.next = self.head
                self.head = node
                self.head.next.prev = node
            else:
                self.head = node
                self.tail = node
            self.size += 1
            return

        if index == self.size:
            if self.size:
                node.prev = self.tail
                node.prev.next = node
                self.tail = node
            else:
                self.tail = node
                self.head = node
            self.size += 1
            return
        
        curr = self.head
        for _ in range(index):
            curr = curr.next

        node.next = curr
        node.prev = curr.prev
        curr.prev.next = node
        curr.prev = node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return

        if index == 0:
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            self.size -= 1
            return

        curr = self.head
        for _ in range(index):
            curr = curr.next

        if curr == self.tail:
            self.tail = curr.prev
            self.tail.next = None
        else:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
        self.size -= 1

