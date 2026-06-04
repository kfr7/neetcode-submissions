from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # first build adj list
        adj = defaultdict(list)
        for edge1, edge2 in edges:
            adj[edge1].append(edge2)
            adj[edge2].append(edge1)

        reached = set()
        current_path = set()
        def dfs(at, came_from = -1):
            if at in current_path:
                return False    # we reached it again
            current_path.add(at)
            reached.add(at)
            # otherwise loop through all the neighbors it can reach other than what we came from
            for neigh in adj[at]:
                if neigh == came_from:
                    continue
                # otherwise we continue with our dfs
                if not dfs(neigh, at):
                    return False
            current_path.remove(at)
            return True
        
        # calling dfs from anywhere should work
        if not dfs(0):
            return False

        return n == len(reached)


