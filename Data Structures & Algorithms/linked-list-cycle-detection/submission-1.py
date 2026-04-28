# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False    # because 2 cycles are needed at least in order to make a cycle
        
        slow = head
        fast = head.next
        while fast is not None:
            if slow is fast:
                return True
            slow = slow.next
            fast = fast.next
            if fast is not None:
                fast = fast.next
        return False
        