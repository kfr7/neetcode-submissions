"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        original_to_new = dict()    # store val: new node

        # first pass is just making sure we clone each one
        def helper(n):
            if n is None:
                return
            # otherwise, try to see if this n is already in our dictionary which mean we traversed it already
            if n.val in original_to_new:
                return original_to_new[n.val]
            
            # otherwise we have work to do
            copy = Node(n.val)
            original_to_new[n.val] = copy
            for neighbor in n.neighbors:
                if copy.neighbors is None:
                    copy.neighbors = []
                copy.neighbors.append(helper(neighbor))
            return copy
        
        return helper(node)



        


        