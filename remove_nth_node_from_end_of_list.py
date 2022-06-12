from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val     
        self.next = next

    def __str__(self) -> str:
        string = '['
        current = self
        while current != None:
            string += f"{current.val},"
            current = current.next
        
        return string + ']'

    @staticmethod
    def from_list(values):
        head = ListNode(values[0])
        current = head
        for value in values[1:]:
            current.next = ListNode(value)
            current = current.next

        return head

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node_indices = []
        current = head
        while current != None:
            node_indices.append(current)
            current = current.next

        node_to_be_removed = node_indices[len(node_indices) - n]
        previous_node = node_indices[len(node_indices) - n - 1]
        if len(node_indices) == n:
            return node_to_be_removed.next

        previous_node.next = node_to_be_removed.next
        node_to_be_removed.next = None

        return head

    def removeNthFromEndTwoPointer(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_head = ListNode(0, head)
        left = dummy_head
        right = head

        # we put the right pointer at n
        while n > 0 and right:
            right = right.next
            n -= 1

        # we iterate to the end of the list, keeping the n distance between left and right
        while right:
            right = right.next
            left = left.next

        left.next = left.next.next
        return dummy_head.next

        

solution = Solution()
result = solution.removeNthFromEnd(ListNode.from_list([1,2,3,4,5]), 2)
print(result)

result = solution.removeNthFromEnd(ListNode.from_list([1]), 1)
print(result)

result = solution.removeNthFromEnd(ListNode.from_list([1,2]), 1)
print(result)

result = solution.removeNthFromEnd(ListNode.from_list([1,2]), 2)
print(result)