from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f'{getattr(self.left, "data") or "None"} <- {self.val} -> {getattr(self.right, "data") or "None"}'
    
    @classmethod
    def generate_from_list(cls, list: List[Optional[int]]) -> Optional["TreeNode"]:
        """
            Generates a tree object from serialized binary tree format

            https://support.leetcode.com/hc/en-us/articles/360011883654-What-does-1-null-2-3-mean-in-binary-tree-representation
        """
        if not List:
            return None
        
        if list[0] is None:
            return None
        
        root = TreeNode(list[0])
        current = root

        i = 1
        queue = deque([current])

        for i in range(1, len(list), 2):
            parent = queue.popleft()

            if list[i] is not None:
                left = TreeNode(list[i])
                parent.left = left
                queue.append(left)

            if i + 1 < len(list) and list[i + 1] is not None:
                right = TreeNode(list[i + 1])
                parent.right = right
                queue.append(right)

        return root