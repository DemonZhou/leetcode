# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        enum = res
        carry = 0
        while l1 and l2 :
            val = l1.val + l2.val
            if carry > 0 :
                val += 1
            if val  >= 10:
                val = val % 10
                carry = 1
            else:
                carry = 0
            enum.next = ListNode(val)
            enum = enum.next
            l1 = l1.next
            l2 = l2.next

        if l1 == None and l2 == None and carry == 1:
            enum.next = ListNode(1)
            return res.next
            
        if l1 != None:
            enum.next = l1
            enum = enum.next
        if l2 != None:
            enum.next = l2
            enum = enum.next
        while enum :
            if carry > 0 :
                enum.val += 1
            if enum.val >= 10:
                enum.val = enum.val % 10
                carry = 1
            else:
                carry = 0
            if enum.next == None and carry == 1:
                enum.next = ListNode(1)
                carry = 0
            enum = enum.next
        return res.next
        


        