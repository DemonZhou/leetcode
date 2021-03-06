import queue as q
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
            
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        que = q.PriorityQueue()
        n = len(lists)
        for i in range(n):
            if lists[i] != None:
                node = lists[i]
                while node:
                    que.put(node.val)
                    node = node.next
        res = ListNode(0)
        enum = res
        while not que.empty():
            l = ListNode(que.get())
            enum.next = l
            enum = l
        return res.next
