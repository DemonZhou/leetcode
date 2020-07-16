# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True

        slow , fast = head , head

        pre = p = None

        while fast and fast.next:
            p = slow

            slow = slow.next
            fast = fast.next.next
            p.next = pre
            pre = p
        
        if fast:
            slow = slow.next

        while p:
            if p.val != slow.val:
                return False
            p = p.next
            slow = slow.next
        return True

