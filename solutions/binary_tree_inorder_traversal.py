from typing import List, Optional
from utilities.tree_node import TreeNode

class BinaryTreeInorderTraversal:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorder_recursive(root, [])
    
    def inorder_recursive(self, node: Optional[TreeNode], traversal: List[int]) -> List[int]:
        """
                     [1]
               [2]        [5]
            [3]   [4]  [6]   [7]
            
            3, 2, 4, 1, 5, 6, 7
        """
        if not node:
            return traversal
        
        self.inorder_recursive(node.left, traversal)
        traversal.append(node.val)
        self.inorder_recursive(node.right, traversal)
    
        return traversal
    
    def inorder_iterative(self, node: Optional[TreeNode]) -> List[int]:
        """
                     [1]
               [2]        [5]
            [3]   [4]  [6]   [7]
            
            traversal: 3, 4, 2, 1, 6, 7, 5
            stack
        """
        if not node:
            return []
        
        traversal = []
        stack = [node.right, node, node.left]
        while stack:
            if not stack[-1]:
                while not stack[-1]:
                    stack.pop()

                while stack[-1] != node:
                    if stack[-1]:
                        traversal.append(stack.pop())
                if stack:
                    traversal.append(stack.pop())
            else:
                stack.append(stack[-1].right)
                stack.append(stack[-1].left)
            
        return traversal
            