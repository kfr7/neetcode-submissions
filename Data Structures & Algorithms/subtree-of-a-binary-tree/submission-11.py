# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def equalityHelper(p, q):
            if p is None and q is None:
                return True
            elif p is None or q is None:
                return False
            elif p.val != q.val:
                return False
            else: # make sure the subtrees are exactly the same
                left_side = equalityHelper(p.left, q.left)
                right_side = equalityHelper(p.right, q.right)
                return left_side and right_side
        def findCommonRoot(node, sub):
            if node is None:
                return False
            else:   # either go left or right and use properties of binary tree
                if sub.val == node.val:
                    answer = equalityHelper(node, sub)
                    if answer is True:
                        return True
                # otherwise we fall through on purpose
                x = findCommonRoot(node.left, sub)
                y = findCommonRoot(node.right, sub)
                if x is True or y is True:
                    return True
                return False

        if subRoot is None:
            if root is None:
                return True
            else:
                return False
        
        return findCommonRoot(root, subRoot)
        

       
       
       
       
       
       
        # return
        # below works only for binary search trees
        # binary trees cannot have repeated values so once there is a match
        # that is where we start searching
        # def findCommonRoot(node, value):
        #     if node is None:
        #         return None
        #     else:   # either go left or right and use properties of binary tree
        #         if value == node.val:
        #             return node
        #         elif value < node.val:
        #             return findCommonRoot(node.left, value)
        #         else:
        #             return findCommonRoot(node.right, value)
        # if subRoot is None:
        #     if root is None:
        #         return True
        #     else:
        #         return False
        # commonRoot = findCommonRoot(root, subRoot.val)
        # if commonRoot is None:
        #     return False
        # # otherwise we have a chance and just need an equality helper
        # def equalityHelper(p, q):
        #     if p is None and q is None:
        #         return True
        #     elif p is None or q is None:
        #         return False
        #     elif p.val != q.val:
        #         return False
        #     else: # make sure the subtrees are exactly the same
        #         left_side = equalityHelper(p.left, q.left)
        #         right_side = equalityHelper(p.right, q.right)
        #         return left_side and right_side
        # return equalityHelper(commonRoot, subRoot)

        