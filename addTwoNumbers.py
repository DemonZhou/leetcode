# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        adder = 0
        
        res = ListNode(0)
        start = res

        while l1 and l2:
            Sum = l1.val + l2.val + adder
            adder = Sum / 10
            start.val = Sum % 10 
            l1 = l1.next
            l2 = l2.next

            if l1 == None and l2 == None :
                if adder != 0:
                    start.next = ListNode(adder)
                    start = start.next
                break
            start.next = ListNode(0)
            start = start.next
        
        while l1:
            Sum = l1.val + adder
            adder = Sum / 10
            start.val = Sum % 10

            l1 = l1.next
            if l1 != None:
                start.next = ListNode(0)
                start = start.next
            if l1 == None and adder != 0:
                start.next = ListNode(adder)
                start = start.next
                break
        
        while l2:
            Sum = l2.val + adder
            adder = Sum / 10
            start.val = Sum % 10

        
            l2 = l2.next
            if l2 != None:
                start.next = ListNode(0)
                start = start.next
            if l2 == None and adder != 0:
                start.next = ListNode(adder)
                start = start.next
                break
            
        return res