from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # first build adjacency matrix so that we know neighbors
        adj = defaultdict(list)
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        visited = set()
        def dfs(i):
            visited.add(i)
            for neighbor in adj[i]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        connected = 0
        for i in range(n):
            if i not in visited:
                connected += 1
                dfs(i)
        return connected

        