# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.sorted = []
        if root:
            values = []
            stack = [root]
            while stack:
                curr = stack.pop()
                values.append(curr.val)
                for child in filter(None, (curr.left, curr.right)):
                    stack.append(child)
            self.sorted = sorted(values, reverse=True)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.sorted.pop()


    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.sorted) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
