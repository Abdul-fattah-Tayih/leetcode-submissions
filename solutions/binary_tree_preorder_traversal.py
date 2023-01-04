from typing import List, Optional
from utilities.tree_node import TreeNode

class BinaryTreePreorderTraversal:
    """
        144. Binary Tree Preorder Traversal

        Given the root of a binary tree, return the preorder traversal of its nodes' values.

        Follow up: Recursive solution is trivial, could you do it iteratively?
    """
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.preorder_iterative(root)
        # return self.preorder_recursive(root, [])
    
    def preorder_recursive(self, node: Optional[TreeNode], traversal) -> List[int]:
        if not node:
            return traversal
        
        traversal.append(node.val)
        self.preorder_recursive(node.left, traversal)
        self.preorder_recursive(node.right, traversal)
        
        return traversal
        
    def preorder_iterative(self, root: Optional[TreeNode]) -> List[int]:
        """
                    [1]
               [2]        [5]
            [3]   [4]  [6]   [7]
            
            We're trying to emulate recursion, which is basically a loop with a stack

            To achieve that, we add the right of the root, then the left of the root

            Then we loop until the stack is empty, and in each iteration we pop,

            and do the same thing, we add right of that popped node, then the left

            We are adding the left last is because we are prioritizing the left side of any subtree,
            
            and the top of the stack is the element that is always popped first, since it is a LIFO data structure
        """
        if not root:
            return []

        traversal_nodes = []
        stack = []
        
        traversal_nodes.append(root.val)
        stack.append(root.right)
        stack.append(root.left)
        while stack:
            next_node = stack.pop()

            if not next_node:
                continue

            traversal_nodes.append(next_node.val)
            
            if next_node.right:
                stack.append(next_node.right)
            
            if next_node.left:
                stack.append(next_node.left)
                
        return traversal_nodes
                