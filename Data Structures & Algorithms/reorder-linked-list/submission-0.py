# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # run slow and fast -> so we git the half of the ll 
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next

        # reverse the second half of the ll
        prev = slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # two pointers first and second to navigate head and prev
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2