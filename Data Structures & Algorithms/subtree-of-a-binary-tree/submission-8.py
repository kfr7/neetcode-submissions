# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if (root is None and subRoot is None) or subRoot is None:
            return True
        
        possibleCommonRoots = []
        # first we need to find the root of the subRoot within the top level root
        # then we just run an isEqual comparer
        def findCommonRoot(search, subRoot):
            if search is None:
                return
            # otherwise let's search
            if search.val == subRoot.val:
                possibleCommonRoots.append(search)
            findCommonRoot(search.left, subRoot)
            findCommonRoot(search.right, subRoot)
        
        findCommonRoot(root, subRoot)
        if len(possibleCommonRoots) == 0:
            return False
                    
        # otherwise we need to just check if they are equal with each other
        def isEqual(node1, node2):
            if node1 is None and node2 is None:
                return True
            if (node1 is None and node2 is not None) or (node1 is not None and node2 is None):
                return False
            # otherwise compare their values
            if node1.val != node2.val:
                return False
            res1 = isEqual(node1.left, node2.left)
            res2 = isEqual(node1.right, node2.right)
            return res1 and res2
        
        for n in possibleCommonRoots:
            if isEqual(n, subRoot):
                return True
        return False

        