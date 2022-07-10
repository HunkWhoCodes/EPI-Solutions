# LC Link: https://leetcode.com/problems/linked-list-cycle/

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
		slow = fast = head
		
		while slow and fast and fast.next:
			fast = fast.next
			if slow == fast:
				return True
			if fast.next:
				fast = fast.next
			slow = slow.next
		
		return False
    	
