from typing import List, Optional
from colorama import Fore

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        result = '['
        current = self
        while current is not None:
            result += f'{current.val}, '
            current = current.next
        
        return result[0:-2] + ']'

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, ListNode): return False

        self_current = self
        object_current = o

        while self_current is not None and object_current is not None:
            self_value = self_current.val
            object_value = object_current.val

            if self_value != object_value:
                return False

            self_current = self_current.next
            object_current = object_current.next

        return True
    
    @classmethod
    def generate_from_list(cls, list: List) -> 'ListNode':
        if len(list) < 1: return None

        head = ListNode(list[0])
        current = head
        for idx, node in enumerate(list):
            if idx > 0:
                current.next = ListNode(node)
                current = current.next
        
        return head

class Solution:
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

test_cases = [
    (ListNode.generate_from_list([1, 2, 3, 4]), ListNode.generate_from_list([2, 1, 4, 3])),
    (ListNode.generate_from_list([]), ListNode.generate_from_list([])),
    (ListNode.generate_from_list([1]), ListNode.generate_from_list([1])),
]

solution = Solution()

for test_case in test_cases:
    input, expected_result = test_case
    actual_result = solution.swapPairs(input)
    if actual_result != expected_result:
        print(f'{Fore.RED} x case failed! input: {input}, expected: {expected_result}, actual: {actual_result}')
    else:
        print(f'{Fore.GREEN} passed! input: {input}')