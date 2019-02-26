# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.i = 0
        self.sorted = []
        if root:
            self.inorder(root)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            self.sorted.append(node.val)
            self.inorder(node.right)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        val = self.sorted[self.i]
        self.i += 1
        return val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.i < len(self.sorted)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
