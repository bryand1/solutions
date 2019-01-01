from ast import literal_eval
from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return

        ret = []
        q = deque([root])
        while True:
            has_values = False
            values = []
            tmp = deque()
            while q:
                node = q.pop()
                val = node.val if node is not None else None
                has_values = has_values or val is not None
                values.append(val)
                tmp.appendleft(node.left if node is not None else None)
                tmp.appendleft(node.right if node is not None else None)
            if has_values:
                ret.extend(values)
                q = tmp
            else:
                break 
        return ret

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return
        lvl = 0
        root = TreeNode(data.pop(0))
        q = deque([root])
        while data:
            items = 2 ** lvl
            while items:
                node = q.pop()
                left = data.pop(0)
                right = data.pop(0)
                if node is not None:
                    node.left = TreeNode(left) if left is not None else None
                    node.right = TreeNode(right) if right is not None else None
                    q.appendleft(node.left)
                    q.appendleft(node.right)
                else:
                    q.appendleft(None)
                    q.appendleft(None)
                items -= 1
            lvl += 1
        return root

# Your Codec object will be instantiated and called as such:

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    codec = Codec()
    print(codec.serialize(root))

    raw = [1, 2, 3, None, None, 4, 5]
    tree = codec.deserialize(raw)
    print(tree.val, tree.left.val, tree.right.val)
