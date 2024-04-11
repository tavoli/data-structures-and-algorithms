import unittest
from doubly_linked_list import Node, DoublyLinkedList

class TestNode(unittest.TestCase):
    def test_initialization(self):
        node = Node(5)
        self.assertEqual(node.val, 5)
        self.assertIsNone(node.next)
        self.assertIsNone(node.prev)
        
    def test_modify_val(self):
        node = Node(10)
        node.val = 20
        self.assertEqual(node.val, 20)
        
    def test_modify_next(self):
        node1 = Node(1)
        node2 = Node(2)
        node1.next = node2
        self.assertIs(node1.next, node2)
        
    def test_modify_prev(self):
        node1 = Node(1)
        node2 = Node(2)
        node1.prev = node2
        self.assertIs(node1.prev, node2)

    def test_initialization_with_next_prev(self):
        node1 = Node(1)
        node2 = Node(2, node1, node1)
        self.assertEqual(node2.val, 2)
        self.assertIs(node2.next, node1)
        self.assertIs(node2.prev, node1)

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index

class TestDoublyLinkedList(unittest.TestCase):
    def test_initialization(self):
        dll = DoublyLinkedList()
        self.assertIsNotNone(dll.head)
        self.assertIsNotNone(dll.tail)
        self.assertEqual(dll.size, 0)

    def test_add_at_head(self):
        dll = DoublyLinkedList()
        dll.addAtHead(1)
        self.assertEqual(dll.head.next.val, 1)
        self.assertEqual(dll.tail.prev.val, 1)
        self.assertEqual(dll.size, 1)
        self.assertIsNone(dll.head.prev)
        self.assertIsNone(dll.tail.next)
        dll.addAtHead(2)
        self.assertEqual(dll.head.next.val, 2)
        self.assertEqual(dll.tail.prev.val, 1)
        self.assertEqual(dll.size, 2)

    def test_add_at_tail(self):
        dll = DoublyLinkedList()
        dll.addAtTail(1)
        self.assertEqual(dll.head.next.val, 1)
        self.assertEqual(dll.tail.prev.val, 1)
        self.assertEqual(dll.size, 1)
        self.assertIsNone(dll.head.prev)
        self.assertIsNone(dll.tail.next)
        dll.addAtTail(2)
        self.assertEqual(dll.head.next.val, 1)
        self.assertEqual(dll.tail.prev.val, 2)
        self.assertEqual(dll.size, 2)

    def test_add_at_index(self):
        dll = DoublyLinkedList()
        dll.addAtIndex(0, 1)
        self.assertEqual(dll.head.next.val, 1)
        self.assertEqual(dll.tail.prev.val, 1)
        self.assertEqual(dll.size, 1)
        dll.addAtIndex(0, 2)
        self.assertEqual(dll.head.next.val, 2)
        self.assertEqual(dll.tail.prev.val, 1)
        self.assertEqual(dll.size, 2)
        dll.addAtIndex(1, 3)
        self.assertEqual(dll.head.next.val, 2)
        self.assertEqual(dll.head.next.next.val, 3)
        self.assertEqual(dll.tail.prev.val, 1)
        self.assertEqual(dll.size, 3)

    def test_delete_at_index(self):
        # delete from empty list
        dll = DoublyLinkedList()
        dll.deleteAtIndex(0)
        self.assertEqual(dll.size, 0)
        # delete from list with one node
        dll.addAtHead(1)
        dll.deleteAtIndex(0)
        self.assertEqual(dll.size, 0)
        # delete from list with two nodes
        dll.addAtHead(1)
        dll.addAtHead(2)
        dll.deleteAtIndex(0)
        self.assertEqual(dll.size, 1)
        self.assertEqual(dll.head.next.val, 1)
        self.assertEqual(dll.tail.prev.val, 1)
        # delete from list with three nodes
        dll.addAtTail(3)
        dll.addAtHead(2)
        dll.deleteAtIndex(1)
        self.assertEqual(dll.size, 2)
        self.assertEqual(dll.head.next.val, 2)
        self.assertEqual(dll.head.next.next.val, 3)
        self.assertEqual(dll.tail.prev.val, 3)
        # delete from list with four nodes
        dll.addAtHead(1)
        dll.addAtTail(4)
        dll.deleteAtIndex(1)
        self.assertEqual(dll.size, 3)
        self.assertEqual(dll.head.next.val, 1)
        self.assertEqual(dll.head.next.next.val, 3)
        self.assertEqual(dll.head.next.next.next.val, 4)
        self.assertEqual(dll.tail.prev.val, 4)

    def test_get_index(self):
        dll = DoublyLinkedList()
        self.assertEqual(dll.get(0), -1)
        dll.addAtHead(1)
        self.assertEqual(dll.get(0), 1)
        dll.addAtHead(2)
        self.assertEqual(dll.get(0), 2)
        self.assertEqual(dll.get(1), 1)
        dll.addAtTail(3)
        self.assertEqual(dll.get(2), 3)
        self.assertEqual(dll.get(3), -1)
        dll.addAtIndex(1, 4)
        self.assertEqual(dll.get(1), 4)
        self.assertEqual(dll.get(2), 1)
        self.assertEqual(dll.get(3), 3)
        dll.deleteAtIndex(1)
        self.assertEqual(dll.get(1), 1)
        self.assertEqual(dll.get(2), 3)
        dll.deleteAtIndex(1)
        self.assertEqual(dll.get(1), 3)
        dll.deleteAtIndex(0)
        self.assertEqual(dll.get(0), 3)
        dll.deleteAtIndex(0)
        self.assertEqual(dll.get(0), -1)

if __name__ == '__main__':
    unittest.main()
