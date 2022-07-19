from typing import Optional
from utilities.list_node import ListNode

class MiddleOfTheLinkedList:
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

if __name__ == '__main__':
    solution = MiddleOfTheLinkedList()
    result = solution.middleNode(ListNode.generate_from_list([1,2,3,4,5]))
    print(result)

    result = solution.middleNode(ListNode.generate_from_list([1,2,3,4,5,6]))
    print(result)