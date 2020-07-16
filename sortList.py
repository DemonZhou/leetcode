# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        slow , fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid =  slow.next
        slow.next = None

        left , right = self.sortList(head) , self.sortList(mid)

        h = dummy = ListNode(0)

        while left and right:
            if left.val < right.val:
                h.next = left
                left = left.next
            else:
                h.next = right
                right = right.next
            h = h.next

        h.next = left or right
        return dummy.next