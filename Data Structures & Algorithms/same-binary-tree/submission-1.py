# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def helper(p, q):
            # if either node is different return False
            if p is None and q is None:
                return True
            elif p is None or q is None:
                return False
            # otherwise we know they are valid nodes
            if p.val != q.val:
                return False
            # if they are the same, assume this helper will work for sub trees
            left_answer = helper(p.left, q.left)
            right_answer = helper(p.right, q.right)
            return left_answer and right_answer
        return helper(p, q)
        