# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        stack = [(root.left, root.right)]
        while stack:
            l, r = stack.pop()
            if l is None and r is None:
                continue
            elif l and r and l.val == r.val:
                stack.append((l.left, r.right))
                stack.append((l.right, r.left))
            else:
                return False

        return True
