# 94. Binary Tree Inorder Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        stack = []
        while True:
            if root:
                stack.append(root)
                root = root.left
            else:
                if not stack:
                    break
                root = stack.pop()
                res.append(root.val)
                root = root.right
        return res
