# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        result = []

        def inorder(node):
            if node is None:
                return 0
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
            return result
        inorder(root)

        values_in_range = [val for val in result if low<=val<=high]
        return sum(values_in_range)        
