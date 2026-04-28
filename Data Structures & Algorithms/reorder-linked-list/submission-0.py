# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # well first we could see what the length of the list is
        # and then we could reverse the second halfs references
        # and then traverse one by one and switch references
        length = 0
        curr = head
        j = 0
        while curr is not None:
            length += 1
            curr = curr.next
            j += 1

        start_reversing_at = length // 2 + 1
        
        curr = head
        i = 0
        prev = None
        while curr is not None:
            if prev is not None:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            elif i == start_reversing_at-1 and i >= 0:
                temp = curr.next
                curr.next = None
                curr = temp
            elif i == start_reversing_at:
                prev = curr
                curr = curr.next
                prev.next = None
            else:
                curr = curr.next
            i += 1

        asc = head
        desc = prev
        while desc is not None and asc is not None:
            temp = asc.next
            asc.next = desc
            asc = temp
            temp = desc.next
            desc.next = asc
            desc = temp
        

        