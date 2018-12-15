# https://leetcode.com/problems/lru-cache/discuss/200656/Python3-(108ms-99.49)-vs.-2-(172ms-37.04)-can-make-a-big-difference-in-runtime.

from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = OrderedDict()
        self.max = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        try:
            value = self.cache[key]
            self.cache.move_to_end(key)
            return value
        except KeyError:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.max:
            self.cache.popitem(last=False)  # Keep size of cache at self.max at most entries.
