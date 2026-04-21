# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # for right side it must be bigger than the max
        # for left side it must be smaller than the min
        def helper(node, leftMaxBound, rightMinBound):
            if node is None:
                return True
            validLeft = True
            if node.left is not None:
                if node.left.val >= node.val or node.left.val >= leftMaxBound or node.left.val <= rightMinBound:
                    validLeft = False
                else:
                    validLeft = helper(node.left, min(leftMaxBound, node.val), rightMinBound)
            validRight = True
            if node.right is not None:
                if node.right.val <= node.val or node.right.val <= rightMinBound or node.right.val >= leftMaxBound:
                    validRight = False
                else:
                    validRight = helper(node.right, leftMaxBound, max(rightMinBound, node.val))
            return validRight and validLeft
        return helper(root, float('inf'), float('-inf'))
            
            
        