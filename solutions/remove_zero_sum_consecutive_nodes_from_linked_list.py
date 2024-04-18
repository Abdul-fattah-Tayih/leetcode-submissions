from typing import Optional
from utilities.list_node import ListNode

class RemoveZeroSumConsecutiveNodesFromLinkedList:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        if not head.next:
            return head

        left = head
        prev = head
        right = head.next
        current_sum = head.val

        while right:
            if right.val + current_sum == 0:
                left = right.next
                prev = left
                right = left.next
                current_sum = 0
            elif right.next and right.val + right.next.val == 0:
                prev.next = right.next.next
                right.next = None
                right = prev

                prev = left
                while prev and prev.next != right:
                    prev = prev.next
            else:
                current_sum += right.val
                right = right.next
                prev = prev.next

        return left
    
if __name__ == "__main__":
    obj = RemoveZeroSumConsecutiveNodesFromLinkedList()
    print(obj.removeZeroSumSublists(ListNode.generate_from_list([1,2,3,-3,-2])))