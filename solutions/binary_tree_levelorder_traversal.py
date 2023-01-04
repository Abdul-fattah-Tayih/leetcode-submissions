from collections import deque
from typing import List, Optional
from utilities.tree_node import TreeNode

class BinaryTreeLevelOrderTraversal:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque()
        queue.append(root)
        traversal = []
        
        while queue:
            nodes_at_this_level = []
            size = len(queue)
            for i in range(size):
                current_node = queue.popleft()
                nodes_at_this_level.append(current_node.val)
                
                if current_node.left:
                    queue.append(current_node.left)
                    
                if current_node.right:
                    queue.append(current_node.right)
                
            traversal.append(nodes_at_this_level)
            
        return traversal