'''
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?


https://leetcode.com/explore/interview/card/google/60/linked-list-5/3064/

'''

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

        p1 = head
        p2 = p1
        p3 = head

        for i in range(n):
            p2 = p2.next
        

        while p2 != None:
            p3 = p1
            p1 = p1.next 
            p2 = p2.next

        if p1 == head:
            head = p1.next
            return head

        p3.next = p1.next
        p1.next = None

        return head
        
        