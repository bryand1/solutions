# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorder(self, root, path):
        if root:
            self.inorder(root.left, path)
            path.append(root.val)
            self.inorder(root.right, path)

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        path = []
        self.inorder(root, path)
        return path

