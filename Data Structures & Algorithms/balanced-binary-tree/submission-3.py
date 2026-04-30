# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(node): # going to return the height, and if it is balanced
            if node is None:
                return 0
            else: # we have at least one child
                height_left = helper(node.left)
                height_right = helper(node.right)
                if height_left is False or height_right is False:
                    return False # just pass it all the way back, stopping point
                else:
                    # both subtrees were balanced, check if difference is acceptable
                    if abs(height_left-height_right) > 1:
                        return False
                    else:
                        return 1 + max(height_left, height_right)
        height = helper(root)
        return height is not False
        