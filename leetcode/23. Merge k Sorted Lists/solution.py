# 23. Merge k Sorted Lists
#
# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
#
# Time: O(n * lg(k))
# Space: O(k)  (data held in the heap)
# 
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
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heappush(heap, (lists[i].val, i))

        root = ListNode(0)
        curr = root
        while heap:
            min_val, i = heappop(heap)
            curr.next = ListNode(min_val)
            curr = curr.next
            lists[i] = lists[i].next
            if lists[i]:
                heappush(heap, (lists[i].val, i))

        return root.next