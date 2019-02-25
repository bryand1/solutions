# 449. Serialize and Deserialize BST
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        serial = []

        def preorder(node):
            if node:
                serial.append(str(node.val))
                preorder(node.left)
                preorder(node.right)
            else:
                serial.append('#')

        preorder(root)
        return ' '.join(serial)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return
        vals = iter(data.split())
        
        def helper():
            val = next(vals)
            if val == '#':
                return
            node = TreeNode(int(val))
            node.left = helper()
            node.right = helper()
            return node

        return helper()


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))