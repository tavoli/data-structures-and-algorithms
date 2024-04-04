import unittest
from linked_list import Node, LinkedList

class TestNode(unittest.TestCase):
    def test_initialization(self):
        node = Node(5)
        self.assertEqual(node.data, 5)
        self.assertIsNone(node.next)
        
    def test_modify_data(self):
        node = Node(10)
        node.data = 20
        self.assertEqual(node.data, 20)
        
    def test_modify_next(self):
        node1 = Node(1)
        node2 = Node(2)
        node1.next = node2
        self.assertIs(node1.next, node2)

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList()

    def test_insert_head_empty_list(self):
        self.linked_list.insert_head(5)
        
        # Check if head and tail point to the same node
        self.assertEqual(self.linked_list.head.data, 5)
        self.assertEqual(self.linked_list.tail.data, 5)
        
    def test_insert_head_non_empty_list(self):
        # Create a linked list with some initial nodes
        self.linked_list.insert_head(2)
        self.linked_list.insert_head(3)
        
        # Insert a new node at the head
        self.linked_list.insert_head(1)
        
        # Check if head is updated correctly
        self.assertEqual(self.linked_list.head.data, 1)
        
        # Check if the next pointer of the new head points to the old head
        self.assertEqual(self.linked_list.head.next.data, 3)
        
    def test_insert_head_update_tail(self):
        # Create a linked list with some initial nodes
        self.linked_list.insert_head(1)
        self.linked_list.insert_head(2)
        
        # Insert a new node at the head
        self.linked_list.insert_head(0)
        
        # Check if tail is updated correctly
        self.assertEqual(self.linked_list.tail.data, 1)
    
    def test_insert_tail_empty_list(self):
        self.linked_list.insert_tail(5)
        
        # Check if head and tail point to the same node
        self.assertEqual(self.linked_list.head.data, 5)
        self.assertEqual(self.linked_list.tail.data, 5)

    def test_insert_tail_non_empty_list(self):
        # Create a linked list with some initial nodes
        self.linked_list.insert_head(1)
        self.linked_list.insert_head(2)
        
        # Insert a new node at the tail
        self.linked_list.insert_tail(3)
        
        # Check if tail is updated correctly
        self.assertEqual(self.linked_list.tail.data, 3)
        
        # Check if the next pointer of the old tail points to the new tail
        self.assertEqual(self.linked_list.head.next.next.data, self.linked_list.tail.data)

    def test_remove_empty_list(self):
        # Test removing from an empty list
        self.assertFalse(self.linked_list.remove(0))

    def test_remove_head(self):
        # Test removing the head node
        self.linked_list.insert_tail(1)
        self.linked_list.insert_tail(2)
        self.assertTrue(self.linked_list.remove(0))
        self.assertEqual(self.linked_list.head.data, 2)

    def test_remove_tail(self):
        # Test removing the tail node
        self.linked_list.insert_tail(1)
        self.linked_list.insert_tail(2)
        self.assertTrue(self.linked_list.remove(1))
        self.assertEqual(self.linked_list.tail.data, 1)

    def test_remove_middle(self):
        # Test removing a node from the middle of the list
        self.linked_list.insert_tail(1)
        self.linked_list.insert_tail(2)
        self.linked_list.insert_tail(3)
        self.assertTrue(self.linked_list.remove(1))
        self.assertEqual(self.linked_list.head.next.data, 3)

    def test_remove_out_of_bounds(self):
        # Test removing from an index beyond the end of the list
        self.linked_list.insert_tail(1)
        self.linked_list.insert_tail(2)
        self.assertFalse(self.linked_list.remove(2))

    def test_get_valid_index(self):
        # Test getting data at a valid index
        self.linked_list.insert_tail(1)
        self.linked_list.insert_tail(2)
        self.assertEqual(self.linked_list.get(0), 1)
        self.assertEqual(self.linked_list.get(1), 2)

    def test_get_negative_index(self):
        # Test getting data with a negative index
        self.linked_list.insert_tail(1)
        self.linked_list.insert_tail(2)
        self.assertEqual(self.linked_list.get(-1), -1)

    def test_get_out_of_bounds_index(self):
        # Test getting data with an out-of-bounds index
        self.linked_list.insert_tail(1)
        self.linked_list.insert_tail(2)
        self.assertEqual(self.linked_list.get(2), -1)

    def test_get_empty_list(self):
        # Test getting data from an empty list
        self.assertEqual(self.linked_list.get(0), -1)

    def test_get_values_empty_list(self):
        # Test getting values from an empty list
        self.assertEqual(self.linked_list.get_values(), [])

    def test_get_values_non_empty_list(self):
        # Test getting values from a non-empty list
        self.linked_list.insert_tail(1)
        self.linked_list.insert_tail(2)
        self.assertEqual(self.linked_list.get_values(), [1, 2])

    def test_get_values_after_modification(self):
        # Test getting values after modification
        self.linked_list.insert_tail(1)
        self.linked_list.insert_tail(2)
        self.linked_list.remove(0)
        self.linked_list.insert_tail(3)
        self.assertEqual(self.linked_list.get_values(), [2, 3])


if __name__ == '__main__':
    unittest.main()

