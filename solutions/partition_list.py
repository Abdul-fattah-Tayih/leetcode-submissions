from typing import Optional
from utilities.list_node import ListNode

class PartitionList:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """
            Question: Given the head of a linked list and a value x, partition it such that all nodes less than x come 
            before nodes greater than or equal to x.
            You should preserve the original relative order of the nodes in each of the two partitions.

            Solution: what we do here is split the linked list in 2, elements less than x are in the left, 
            and on the right we have elements that are greater than or equal to x in order
            which means that as we go we append those items directly on each side
        """
        if head is None: return None

        current = head
        left_head = left_current = None
        right_head = right_current = None
        while current is not None:
            if current.val < x:
                if left_head is None:
                    left_head = ListNode(current.val)
                    left_current = left_head
                else:
                    left_current.next = ListNode(current.val)
                    left_current = left_current.next
            else:
                if right_head is None:
                    right_head = ListNode(current.val)
                    right_current = right_head
                else:
                    right_current.next = ListNode(current.val)
                    right_current = right_current.next

            current = current.next

        if left_head:
            # connect left list to the right list
            left_current.next = right_head
        else:
            # in some cases left might be None, so we handle that
            return right_head

        return left_head


if __name__ == '__main__':
    solution = PartitionList()
    print(solution.partition(ListNode.generate_from_list([1,4,3,2,5,2]), 3)) # should be [1,2,2,4,3,5]
    print(solution.partition(ListNode.generate_from_list([2,1]), 2)) # should be [1,2]
    print(solution.partition(ListNode.generate_from_list([]), 0)) # should be [1,2]
    print(solution.partition(ListNode.generate_from_list([1,4,3,0,2,5,2]), 3)) # should be [0,1,2,2,4,3,5]
    print(solution.partition(ListNode.generate_from_list([1]), 0)) # should be [0,1,2,2,4,3,5]
