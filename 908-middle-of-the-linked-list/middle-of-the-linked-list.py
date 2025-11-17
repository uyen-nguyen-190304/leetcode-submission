# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Two pointers
        slow = fast = head

        # Move fast by two steps and slow by 1 step
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow will be at the middle when fast reaches the end
        return slow