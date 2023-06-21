from utilities.tree_node import TreeNode

def rob(root):
    if not root:
        return 0
  
    def traversal(node):
        if not node:
            return [0, 0]

        left = traversal(node.left)
        right = traversal(node.right)

        with_root = node.data + left[1] + right[1]
        without_root = max(left) + max(right)

        return [with_root, without_root]

    return max(traversal(root))

# [9,7,11,1,8,10,12]
#                           9
#                   7               11
#               1       8       10      12
#
# 40
if __name__ == '__main__':
    tree = TreeNode(9)
    tree.left = TreeNode(7)
    tree.left.left = TreeNode(1)
    tree.left.right = TreeNode(8)
    tree.right = TreeNode(11)
    tree.right.left = TreeNode(10)
    tree.right.right = TreeNode(12)

    rob(tree)