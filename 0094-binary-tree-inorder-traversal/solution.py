# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        if not root:
            return []

        A = self.inorderTraversal(root.left)
        res.extend(A)
        res.append(root.val)
        C = self.inorderTraversal(root.right)
        res.extend(C)

        return res
        
