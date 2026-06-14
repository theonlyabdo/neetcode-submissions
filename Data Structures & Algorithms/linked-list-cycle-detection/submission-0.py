# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()

        h = head
        while h:
            if h in seen:
                return True
            seen.add(h)
            h = h.next
        
        return False