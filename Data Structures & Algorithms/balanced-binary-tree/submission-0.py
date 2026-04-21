# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            if not root:
                return (0, True)
            left_height, left_result = helper(root.left)
            right_height, right_result = helper(root.right)

            if not left_result or not right_result:
                return 0, False

            if left_height - right_height > 1 or right_height - left_height > 1:
                return 0, False
            
            return 1 + max(left_height, right_height), True
        
        result = helper(root)
        return result[1]
            
            

        