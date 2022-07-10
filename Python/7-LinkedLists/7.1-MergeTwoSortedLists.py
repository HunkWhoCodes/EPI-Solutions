# LC Link: https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, L1: Optional[ListNode], L2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not L1:
            return L2
        if not L2:
            return L1

        dummy = ListNode()
        tail = dummy

        while L1 and L2:
            if L1.val < L2.val:
                tail.next = L1
                L1 = L1.next
            else:
                tail.next = L2
                L2 = L2.next
            tail = tail.next

        if L1 and not L2:
            tail.next = L1
        if L2 and not L1:
            tail.next = L2

        return dummy.next



