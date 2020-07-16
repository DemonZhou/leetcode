# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head

        while True:
            if not slow :
                return None

            slow = slow.next
            

            if fast.next and fast.next.next:
                fast = fast.next.next
            else:
                return None

            if slow == fast:
                break
            
        
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow