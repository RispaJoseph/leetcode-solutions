# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def inorder(node):
            if node is None:
                return 0
            if node.left is None:
                return 1 + inorder(node.right)
            if node.right is None:
                return 1 + inorder(node.left)
            if node.left is None and node.right is None:
                return 1
            return 1 + min(inorder(node.left), inorder(node.right))

        return inorder(root)
        
