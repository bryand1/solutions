# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.q = deque()
        if root:
            self.inorder(root)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            self.q.append(node.val)
            self.inorder(node.right)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.q.popleft()

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.q) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
