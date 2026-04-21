# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        biggest_diameter = 0
        def helper(r):
            if not r:
                return 0
            nonlocal biggest_diameter
            left_result, right_result = helper(r.left), helper(r.right)
            result = 1 + left_result + right_result
            biggest_diameter = max(biggest_diameter, result)
            return 1 + max(left_result, right_result)
        helper(root)
        return biggest_diameter-1


        
        