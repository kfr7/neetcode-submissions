"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copies = dict()
        dummy = Node(1)
        prev = dummy
        curr = head
        while curr is not None:
            new_node = Node(curr.val)
            prev.next = new_node
            copies[curr] = new_node
            prev = new_node
            curr = curr.next
        
        # now that all the "nexts" are created already
        curr = head
        while curr is not None:
            if curr.next:
                copies[curr].next = copies[curr.next]
            if curr.random:
                copies[curr].random = copies[curr.random]
            curr = curr.next

        print('deep copy');
        deep = dummy.next
        while deep is not None:
            print(deep.val, deep, deep.next)
            deep = deep.next
        testing = head
        print('----')
        while testing is not None:
            print(testing.val, testing, testing.next)
            testing = testing.next 
        return dummy.next
        