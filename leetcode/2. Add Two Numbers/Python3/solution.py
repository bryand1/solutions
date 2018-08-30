# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        _sum = 0
        mul = 1
        while l1 and l2:
            _sum += l1.val * mul
            _sum += l2.val * mul
            l1 = l1.next
            l2 = l2.next
            mul *= 10
        while l1:
            _sum += l1.val * mul
            l1 = l1.next
            mul *= 10
        while l2:
            _sum += l2.val * mul
            l2 = l2.next
            mul *= 10
        rev = str(_sum)[::-1]
        ll = ListNode(int(rev[0]))
        cur = ll
        for i in range(1, len(rev)):
            prev = cur
            cur = ListNode(int(rev[i]))
            prev.next = cur
        return ll

