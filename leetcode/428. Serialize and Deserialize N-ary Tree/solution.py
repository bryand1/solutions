"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        ret = []

        def preorder(node):
            if node:
                ret.append(str(node.val))
                for child in node.children:
                    preorder(child)
                ret.append('#')

        preorder(root)
        return ' '.join(ret)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return

        vals = iter(data.split())
        root = Node(int(next(vals)), [])

        def helper(node):
            while True:
                val = next(vals)
                if val == '#':
                    break
                child = Node(int(val), [])
                node.children.append(child)
                helper(child)

        helper(root)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
