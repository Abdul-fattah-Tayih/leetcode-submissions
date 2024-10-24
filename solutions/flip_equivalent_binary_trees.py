from typing import Optional
from utilities.tree_node import TreeNode


class FlipEquivalentBinaryTrees:
    """
        951. Flip Equivalent Binary Trees

        For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.

        A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.

        Given the roots of two binary trees root1 and root2, return true if the two trees are flip equivalent or false otherwise.
    """
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        """
            Simple DFS solution

            To check whether or not the 2 trees were flipped versions of each other, and since both trees are binary, it means in each level

            The values of the children of each node must be either the same or flipped, any other way means that the trees were not flipped and are completely different

            So we DFS through both trees at the same time, and do the following:
                - if the current nodes for either tree are not equal, we return False, the criteria is:
                    - one of them is None and the other is not
                    - their values don't match if both are not None
                - If the values match, we redo the check for the next level, but we don't necessarily move the same way through the trees
                    - if the lefts of the both of the current nodes match, it means the next level isn't flipped, and we navigate both lefts of the trees
                        - node1 left
                        - node2 right
                    - if the lefts of the current nodes don't match, then the next level is either flipped or doesn't match, regardless we navigate
                        - node1 left
                        - node2 right
        """
        if not root1 or not root2:
            return root1 == root2

        def dfs(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
            if not node1 and not node2:
                return True

            if not node1 and node2:
                return False
            
            if not node2 and node1:
                return False

            if node1.val != node2.val:
                return False
            
            if node1.left == None and node2.left == None:
                left_result = dfs(node1.left, node2.left)
                right_result = dfs(node1.right, node2.right)
            elif node1.left != None and node2.left != None and node1.left.val == node2.left.val:
                left_result = dfs(node1.left, node2.left)
                right_result = dfs(node1.right, node2.right)
            else:
                left_result = dfs(node1.left, node2.right)
                right_result = dfs(node1.right, node2.left)

            return left_result and right_result

        return dfs(root1, root2)

if __name__ == '__main__':
    obj = FlipEquivalentBinaryTrees()

    result = obj.flipEquiv(
        TreeNode.generate_from_list([1,2,3,4,5,6,None,None,None,7,8]),
        TreeNode.generate_from_list([1,3,2,None,6,4,5,None,None,None,None,8,7])
    )

    print(result)

    result = obj.flipEquiv(
        TreeNode.generate_from_list([0,None,1]),
        TreeNode.generate_from_list([0,None,1]),
    )

    print(result)