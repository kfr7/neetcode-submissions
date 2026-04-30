# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # this is simply at every node, add the max height of both children
        largest_diameter = 0
        def helper(node):
            nonlocal largest_diameter
            if node is None:
                return 0
            else:
                # check if this current node's left and right are larger
                height_left = helper(node.left)
                height_right = helper(node.right)
                largest_diameter = max(largest_diameter, height_left + height_right)
                return 1 + max(height_left, height_right)
        helper(root)
        return largest_diameter
        