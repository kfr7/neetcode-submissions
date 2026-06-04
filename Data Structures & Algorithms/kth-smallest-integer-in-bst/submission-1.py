# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # let's just traverse the whole thing using inorder traversal
        # then iterate through the traversal k times and return that element
        inorder = []
        def helper(node):
            if node is None:
                return
            helper(node.left)
            if len(inorder) == k:
                return
            inorder.append(node.val)
            if len(inorder) == k:
                return  # just break out
            helper(node.right)
        
        helper(root)
        print(inorder)
        return inorder[-1]
        