# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def inorder_traversal(node):
            if node is None:
                return []
            return inorder_traversal(node.left)+[node.val]+inorder_traversal(node.right)
        return len(inorder_traversal(root))


        
