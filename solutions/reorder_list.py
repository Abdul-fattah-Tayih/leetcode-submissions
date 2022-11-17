from typing import Optional
from utilities.list_node import ListNode

class ReorderList:
    """
        143. Reorder List

        You are given the head of a singly linked-list. The list can be represented as:

        L0 → L1 → … → Ln - 1 → Ln

        Reorder the list to be on the following form:

        L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

        You may not modify the values in the list's nodes. Only nodes themselves may be changed.
    """
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge two halfs
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

if __name__ == '__main__':
    object = ReorderList()

    linked_list = ListNode.generate_from_list([1,2,3,4])
    object.reorderList(linked_list)
    print(linked_list)
    
    linked_list = ListNode.generate_from_list([1,2,3,4,5])
    object.reorderList(linked_list)
    print(linked_list)
    
    linked_list = ListNode.generate_from_list([1,2,3,4,5,6,7])
    object.reorderList(linked_list)
    print(linked_list) # should be [1,7,2,6,3,5,4]
    
    linked_list = ListNode.generate_from_list([1,2,3,4,5,6,7,8,9,10,11])
    object.reorderList(linked_list)
    print(linked_list) # should be [1,11,2,10,3,9,4,8,5,7,6]
    