# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Define two pointers
        slow = fast = head

        # Chasing to see if there is a loop inside the linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # If the two pointers meet -> there is a cycle
            if slow == fast:
                return True
        
        # fast reaches the end -> no cycle
        return False