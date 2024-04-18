from typing import Optional
from utilities.tree_node import TreeNode

class DiameterOfBinaryTree:
    """
        543. Diameter of Binary Tree

        Given the root of a binary tree, return the length of the diameter of the tree.

        The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

        The length of a path between two nodes is represented by the number of edges between them.
    """
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        
        def depth(node):
            if not node:
                return 0
            
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            
            # Calculate diameter at each node and update self.diameter
            self.diameter = max(self.diameter, left_depth + right_depth)
            
            return max(left_depth, right_depth) + 1
        
        depth(root)
        return self.diameter


if __name__ == "__main__":
    obj = DiameterOfBinaryTree()
    tree = TreeNode.generate_from_list([4,-7,-3,None,None,-9,-3,9,-7,-4,None,6,None,-6,-6,None,None,0,6,5,None,9,None,None,-1,-4,None,None,None,-2])
    print(obj.diameterOfBinaryTree(tree))