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
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        linked_list_indices = {}

        index = 0
        current = head
        while current != None:
            linked_list_indices[index] = current
            current = current.next
            index += 1

        middle = len(linked_list_indices) // 2

        return linked_list_indices[middle]

solution = Solution()
result = solution.middleNode(ListNode.from_list([1,2,3,4,5]))
print(result)

result = solution.middleNode(ListNode.from_list([1,2,3,4,5,6]))
print(result)