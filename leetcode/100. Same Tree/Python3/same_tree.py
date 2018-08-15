# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True

        stack = [(p, q)]
        while stack:
            l, r = stack.pop()
            if l is None and r is None:
                continue
            elif l and r and l.val == r.val:
                stack.append((l.left, r.left))
                stack.append((l.right, r.right))
            else:
                return False

        return True
