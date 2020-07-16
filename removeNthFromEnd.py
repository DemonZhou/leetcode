# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        l1 = dummy
        l2 = l1

        for i in range(n + 1):
            l2 = l2.next
        
        while l2:
            l1 = l1.next
            l2 = l2.next
        
        l1.next = l1.next.next

        return dummy.next