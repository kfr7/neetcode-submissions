# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if root is None:
            return res
        queue = [root]
        next_level = []
        while len(queue) != 0:
            curr_level_values = []
            for element in queue:
                curr_level_values.append(element.val)
                if element.left:
                    next_level.append(element.left)
                if element.right:
                    next_level.append(element.right)
            res.append(curr_level_values)
            queue = next_level
            next_level = []
        return res



        