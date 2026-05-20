from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(set)
        for time in times:
            adj[time[0]].add((time[1], time[2]))
        
        heap = [(0, k)]
        distance = [-1] * n
        visited = set()

        while len(heap) != 0:
            time, node = heapq.heappop(heap)
            if node in visited:
                continue
            print('node:', node)
            visited.add(node)
            distance[node-1] = time
            for neigh, t in adj[node]:
                heapq.heappush(heap, (time+t, neigh))
        
        for d in distance:
            if d == -1:
                return -1
        return max(distance)

        







        