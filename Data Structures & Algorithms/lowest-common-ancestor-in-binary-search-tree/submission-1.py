# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def findIt(node, val):
            if node is None:
                return False
            if node.val == val:
                return True
            else: # lets continue searching for it
                if val < node.val:
                    return findIt(node.left, val)
                else:
                    return findIt(node.right, val)

        def helper(node, p, q):
            if node is None:
                return None # TODO THINK ABOUT WHAT TO RETURN
            if node.val < p.val and node.val < q.val:
                return helper(node.right, p, q)
            elif node.val > p.val and node.val > q.val:
                return helper(node.left, p, q)
            # and then we see if we are splitting
            elif node.val > p.val and node.val < q.val:
                found_right = findIt(node.right, q.val) 
                found_left = findIt(node.left, p.val)
                if found_right and found_left:
                    return node
            elif node.val < p.val and node.val > q.val:
                found_right = findIt(node.right, p.val) 
                found_left = findIt(node.left, q.val)
                if found_right and found_left:
                    return node
            # otherwise one of these are equal to it
            elif node.val == p.val:
                if node.val < q.val:
                    if findIt(node.right, q.val):
                        return node
                    # it must find it
                else:
                     if findIt(node.left, q.val):
                        return node
                    # it must find it
            elif node.val == q.val:
                if node.val < p.val:
                    if findIt(node.right, p.val):
                        return node
                    # it must find it
                else:
                     if findIt(node.left, p.val):
                        return node
                    # it must find it
        return helper(root, p, q)
            

        