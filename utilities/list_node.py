from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    """
        Generic singly linked list implementation in leetcode, also has some quality of life methods 
        like implementing __str__ and __eq__, as well as a static method to generate a linked list for a normal list
    """
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        result = '['
        current = self
        while current is not None:
            result += f'{current.val}, '
            current = current.next
        
        return result[0:-2] + ']'

    def __repr__(self) -> str:
        return f'ListNode({self.__str__()})'

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
    def generate_from_list(cls, list: List) -> Optional['ListNode']:
        if len(list) < 1: return None

        head = ListNode(list[0])
        current = head
        for idx, node in enumerate(list):
            if idx > 0:
                current.next = ListNode(node)
                current = current.next
        
        return head