from collections import defaultdict

class Solution:
    # okay i know this is a union find problem as well
    class UnionFind:
        def __init__(self, x):
            self.parent = [i for i in range(x)]
            self.rank = [0] * x
        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        def union(self, x, y):
            root_x = self.find(x)
            root_y = self.find(y)
            if root_x == root_y:
                return
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_x] = root_y
                self.rank[root_y] += 1

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # now we can just loop through each edge once and keep unioning them
        uf = self.UnionFind(n)
        for edge in edges:
            uf.union(edge[0], edge[1])
        # now we have each union so we just need to find the number of different roots
        roots = set()
        for i in range(n):
            roots.add(uf.find(i))
        return len(roots)










        # first build adjacency matrix so that we know neighbors
        # adj = defaultdict(list)
        # for edge in edges:
        #     adj[edge[0]].append(edge[1])
        #     adj[edge[1]].append(edge[0])
        # visited = set()
        # def dfs(i):
        #     visited.add(i)
        #     for neighbor in adj[i]:
        #         if neighbor not in visited:
        #             dfs(neighbor)
        
        # connected = 0
        # for i in range(n):
        #     if i not in visited:
        #         connected += 1
        #         dfs(i)
        # return connected

        