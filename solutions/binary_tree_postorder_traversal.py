from typing import List, Optional
from utilities.tree_node import TreeNode

class BinaryTreePostOrderTraversal:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.postorder_recursive(root, [])
        
    def postorder_recursive(self, node: Optional[TreeNode], traversal: List[int]):
        if not node:
            return traversal
        
        self.postorder_recursive(node.left, traversal)
        self.postorder_recursive(node.right, traversal)
        traversal.append(node.val)
        
        return traversal