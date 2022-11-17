from typing import Optional
from utilities.list_node import ListNode

class LinkedListCycle:
    """
        Question 141 Linked List Cycle

        Given head, the head of a linked list, determine if the linked list has a cycle in it.

        There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

        Return true if there is a cycle in the linked list. Otherwise, return false.
    """
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
            O(n) time and space complexities

            This solution stores the object identifiers in a list
            and checks whether the current node has been passed before, 
            97% faster than other solutions
        """
        passed_nodes = set()
        position = 0
        current = head

        while current is not None:
            if id(current) in passed_nodes:
                return True

            passed_nodes.add(id(current))
            position += 1
            current = current.next
        
        return False

    def hasCycleOptimal(self, head: Optional[ListNode]):
        """
            O(1), Floyd's Turtoise and Hare algorithm (fast/slow pointers)

            The idea here is we're putting 2 pointers at the start, the slow pointer

            Would move by 1 element, and the fast one will move by 2, and in each iteration we

            compare the objects on each pointer and if they match, then there exists a cycle
        """

        if not head:
            return False

        slow_pointer = head
        fast_pointer = head

        while fast_pointer and fast_pointer.next:
            if slow_pointer is fast_pointer:
                return True

            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

        return False

if __name__ == '__main__':
    object = LinkedListCycle()

    linked_list = ListNode.generate_from_list([3,2,0,-4])
    linked_list.get_last_node().next = linked_list

    print(object.hasCycle(linked_list))
    print(object.hasCycleOptimal(linked_list))

    linked_list = ListNode.generate_from_list([1, 2])
    linked_list.get_last_node().next = linked_list

    print(object.hasCycle(linked_list))
    print(object.hasCycleOptimal(linked_list))

    linked_list = ListNode.generate_from_list([1])
    print(object.hasCycle(linked_list))
    print(object.hasCycleOptimal(linked_list))