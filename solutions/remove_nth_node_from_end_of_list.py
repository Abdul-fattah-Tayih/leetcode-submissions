from typing import Optional
from utilities.list_node import ListNode

class RemoveNthNodeFromEndOfList:
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

        
if __name__ == '__main__':
    solution = RemoveNthNodeFromEndOfList()
    result = solution.removeNthFromEnd(ListNode.generate_from_list([1,2,3,4,5]), 2)
    print(result)

    result = solution.removeNthFromEnd(ListNode.generate_from_list([1]), 1)
    print(result)

    result = solution.removeNthFromEnd(ListNode.generate_from_list([1,2]), 1)
    print(result)

    result = solution.removeNthFromEnd(ListNode.generate_from_list([1,2]), 2)
    print(result)