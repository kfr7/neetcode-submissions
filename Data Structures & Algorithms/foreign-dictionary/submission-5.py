import heapq

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # we can build a topological graph
        # after we build the graph, traverse it... te amo mi amor lindo papasito sabroso jejeje :)
        adj = defaultdict(set)
        for i in range(1, len(words)):
            previous_word = words[i-1]
            current_word = words[i]
            # edge case
            if len(previous_word) > len(current_word):
                for j in range(len(previous_word)):
                    if j == len(current_word):
                        # then the prefixes were the same but a is longer so return empty string
                        return ''
                    # otherwise we are within bounds
                    if previous_word[j] != current_word[j]:
                        adj[previous_word[j]].add(current_word[j])
                        break
                    # if they are equal we keep going
            else:   # the current word is the same or longer
                for j in range(len(previous_word)):
                    # j will never be out of range of current_word
                    if previous_word[j] != current_word[j]:
                        adj[previous_word[j]].add(current_word[j])
                        break
                    # otherwise if they were all the same we can't get any info out of this
       
        print('adj:', adj)
        # now, we can run topological sort on this adj list we have created
        # lets only run dfs on nodes that have no incoming edges
        visited = set()
        current_path = set()
        def dfs(node, build):
            if node in visited:
                return build
            print('node:', node)
            if node in current_path:    # we are in a cycle
                return ""
            # otherwise we add it to the current_path
            current_path.add(node)
            print('adj[node]:', adj[node])
            for neighbor in adj[node]:
                if dfs(neighbor, build) == "":
                    return ""
            current_path.remove(node)
            build.append(node)
            print(build)
            visited.add(node)
            return build
        
        # first lets find the nodes that are all zeros
        chars_known = set()
        for word in words:
            for ch in word:
                chars_known.add(ch)
        
        # now let's run dfs until everything is done
        result = []
        print('chars_known:', chars_known)
        for ch in chars_known:
            if ch not in visited:
                x = dfs(ch, [])
                if x == "":
                    return ""
                print('x:', x)
                print('res before and result after')
                print('res1:', result)
                result.extend(x)
                print('res2:', result)
        
        return ''.join(result[::-1])
        


        
        
        
        
        
        
        
        





        
        
        
        
        
        
        
        # adj = defaultdict(set)
        # incoming_per_node = defaultdict(int)
        # for i in range(1, len(words)):
        #     # compare both words and the first difference we know is an edge from->to
        #     # if left word is shorter or equal
        #     if len(words[i-1]) <= len(words[i]):
        #         for j in range(len(words[i])):
        #             if j < len(words[i-1]) and words[i-1][j] != words[i][j]:
        #                 adj[words[i-1][j]].add(words[i][j])
        #                 if words[i-1][j] not in incoming_per_node:
        #                     incoming_per_node[words[i-1][j]] = 0
        #                 incoming_per_node[words[i][j]] += 1
        #                 # then we build an edge
        #                 break
        #             elif j == len(words[i-1]):
        #                 adj[words[i-1][j-1]].add(words[i][j])
        #                 if words[i-1][j-1] not in incoming_per_node:
        #                     incoming_per_node[words[i-1][j-1]] = 0
        #                 incoming_per_node[words[i][j]] += 1
        #     else:   # we know the left word is longer, differentiating char will never be after shorter word
        #          for j in range(len(words[i])):
        #             if words[i-1][j] != words[i][j]:
        #                 adj[words[i-1][j]].add(words[i][j])
        #                 if words[i-1][j] not in incoming_per_node:
        #                     incoming_per_node[words[i-1][j]] = 0
        #                 incoming_per_node[words[i][j]] += 1
        #                 break
        
        # # now that we have this, lets build a min heap of incoming edge count per node
        # # simply, go through the incoming and build a min heap
        # visited = set()
        # heap = []
        # for k, v in incoming_per_node.items():
        #     heapq.heappush(heap, (v, k))
        
        # res = []
        # while len(heap) != 0:
        #     _, node = heapq.heappop(heap)
        #     if node in visited:
        #         continue
        #     visited.add(node)
        #     # otherwise add it to the result and decrement the count of everything else
        #     res.append(node)
        #     for neighbor in adj[node]:
        #         if neighbor not in visited:
        #             # then lets decrement them and add them to the heap
        #             incoming_per_node[neighbor] -= 1
        #             heapq.heappush(heap, (incoming_per_node[neighbor], neighbor))
        # return "".join(res)



        