# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        
        def max_depth(node: Optional[TreeNode]) -> int:
            nonlocal diameter
            if not node:
                return 0
            left = max_depth(node.left)
            right = max_depth(node.right)
            diameter = max(diameter, left + right)
            return 1 + max(left, right)
            
        max_depth(root)
        return diameter