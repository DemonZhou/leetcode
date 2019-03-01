# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def InsertNode(self,s,node) :
        """
        :type start: ListNode node: ListNode
        """
        start = s
        while start :
            if start.next != None and start.val <= node.val and start.next.val >= node.val:
                temp = start.next # keep the original next node
                start.next = node
                node.next = temp
                break
            if start.next == None and start.val <= node.val:
                node.next = None
                start.next = node
                break
            start = start.next
        
            
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        n = len(lists)
        if n == 0:
            return None
        node = lists[0]
        start = node
        for i in range(1,n):
            lnode = lists[i]
            if start == None:
                    start = lnode
            while lnode:
                t = lnode.next # keep the next node that needs to be inserted
                if lnode.val < start.val:
                    lnode.next = start
                    start = lnode
                else:
                    self.InsertNode(start,lnode)
                lnode = t

        return start
