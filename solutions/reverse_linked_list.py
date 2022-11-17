from typing import Optional
from utilities.list_node import ListNode

class ReverseLinkedList:
    """
        206. Reverse Linked List

        Given the head of a singly linked list, reverse the list, and return the reversed list.
    """
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        reversed_linked_list = None
        current = head
        while current is not None:
            reversed_linked_list = ListNode(current.val, reversed_linked_list)
            current = current.next

        return reversed_linked_list

if __name__ == '__main__':
    object = ReverseLinkedList()

    linked_list = ListNode.generate_from_list([3,2,0,-4])
    print(object.reverseList(linked_list))

    linked_list = ListNode.generate_from_list([1, 2])
    print(object.reverseList(linked_list))

    linked_list = ListNode.generate_from_list([])
    print(object.reverseList(linked_list))
