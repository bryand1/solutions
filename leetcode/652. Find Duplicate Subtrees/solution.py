# LeetCode 652. Find Duplicate Subtrees
#
# Given a binary tree, return all duplicate subtrees. For each kind of duplicate
# subtrees, you only need to return the root node of any one of them.
#
# Two trees are duplicate if they have the same structure with same node values.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict


class Solution(object):

    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """

        def maketuple(root):
            if root:
                t = root.val, maketuple(root.left), maketuple(root.right)
                trees[t].append(root)
                return t

        trees = defaultdict(list)
        maketuple(root)
        return [root[0] for root in trees.values() if root[1:]]
