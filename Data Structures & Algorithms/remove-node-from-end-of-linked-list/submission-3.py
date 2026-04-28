# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None and n > 0:
            return None
        
        # otherwise lets get the length of the list
        p = head
        length = 0
        while p is not None:
            length += 1
            p = p.next
        

        target_to_remove = length-n
        counter = 0
        prev = None
        curr = head
        while curr is not None:
            print(curr.val)
            if counter == target_to_remove:
                # if there is a previous and a next
                if prev:
                    prev.next = curr.next
                else:
                    head = curr.next
                temp = curr.next
                curr.next = None
                curr = temp
            else:
                prev = curr
                curr = curr.next
            counter += 1
        return head
        
        