# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorder(self, node, path):
        if node:
            self.postorder(node.left, path)
            self.postorder(node.right, path)
            path.append(node.val)

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        path = []
        self.postorder(root, path)
        return path

