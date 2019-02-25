# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from heapq import heappush, heappop

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        k = len(lists)
        pointers = [0] * k
        heap = []
        for i in range(k):
            if lists[i]:
                pointers[i] = lists[i]
                heappush(heap, (pointers[i].val, i))

        root = ListNode(0)
        res = root
        while heap:
            min_val, i = heappop(heap)
            res.next = ListNode(min_val)
            res = res.next
            pointers[i] = pointers[i].next
            if pointers[i]:
                heappush(heap, (pointers[i].val, i))

        return root.next
