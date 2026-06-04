from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # lets create an adjacency list
        adj = defaultdict(list)
        inbound = defaultdict(int)
        for after, before in prerequisites:
            adj[before].append(after)
            if before not in inbound:
                inbound[before] = 0
            inbound[after] += 1
        
        # identify which are all the starting ones
        queue = []
        for k, v in inbound.items():
            if v == 0:
                queue.append(k)
                
        # now we can loop through the queue and decrease inbound
        while len(queue) != 0:
            prereq = queue.pop()
            del inbound[prereq]
            for after_course in adj[prereq]:
                inbound[after_course] -= 1
                if inbound[after_course] == 0:
                    queue.append(after_course)
        
        if len(inbound) == 0:
            return True
        else:
            return False

        