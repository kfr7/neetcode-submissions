# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result = []
        queue = [root]
        while len(queue) != 0:
            this_row = []
            new_queue = []
            for n in queue:
                this_row.append(n.val)
                if n.left is not None:
                    new_queue.append(n.left)
                if n.right is not None:
                    new_queue.append(n.right)
            result.append(this_row)
            queue = new_queue[:]
        return result

        