# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorder(self, node, path):
        if node:
            path.append(node.val)
            self.preorder(node.left, path)
            self.preorder(node.right, path)

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        path = []
        self.preorder(root, path)
        return path

