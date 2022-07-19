from typing import Optional
from unittest import main
from utilities.list_node import ListNode

class SwapNodesInLinkedList:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return None

        current = head
        while current is not None:
            temp = current.val
            
            try:
                current.val = current.next.val
                current.next.val = temp
                current = current.next.next
            except (NameError, AttributeError) as e:
                break
        
        return head

if __name__ == '__main__':
    test_runner = main('tests.test_swap_nodes_in_linked_list', exit=False)