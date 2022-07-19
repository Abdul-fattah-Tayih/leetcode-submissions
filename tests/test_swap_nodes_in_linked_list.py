from unittest import TestCase

from solutions.swap_nodes_in_linked_list import SwapNodesInLinkedList
from utilities.list_node import ListNode

class TestSwapNodesInLinkedList(TestCase):
    def setUp(self) -> None:
        self.solution_object = SwapNodesInLinkedList()

    def test_1(self):
        result = self.solution_object.swapPairs(ListNode.generate_from_list([1, 2, 3, 4]))
        self.assertEqual(result, ListNode.generate_from_list([2, 1, 4, 3]))

    def test_2(self):
        result = self.solution_object.swapPairs(ListNode.generate_from_list([]))
        self.assertEqual(result, ListNode.generate_from_list([]))

    def test_3(self):
        result = self.solution_object.swapPairs(ListNode.generate_from_list([1]))
        self.assertEqual(result, ListNode.generate_from_list([1]))