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
                return
            
            # otherwise we have work to do
            original_to_new[n.val] = Node(n.val)
            for neighbor in n.neighbors:
                helper(neighbor)
    
        helper(node)
        # second pass lets actually connect the neighbors
        visited = set()
        def helper2(n):
            if n is None:
                return
            if n.val in visited:
                return
            visited.add(n.val)
            new = original_to_new[n.val]
            for neighbor in n.neighbors:
                if new.neighbors is None:
                    new.neighbors = []
                # then fall through
                new.neighbors.append(original_to_new[neighbor.val])
                helper2(neighbor)
        
        helper2(node)
        
        return original_to_new[node.val]


        


        