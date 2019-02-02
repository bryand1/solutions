from collections import defaultdict, OrderedDict


class LFUCache:

    def __init__(self, capacity):
        self.k = capacity
        self.cache = {}
        self.freq = defaultdict(OrderedDict)
        self.least_freq = 1
    
    def _evict(self):
        key, _ = self.freq[self.least_freq].popitem(last=False)
        del self.cache[key]
    
    def _update(self, key, new_v=None):
        freq, v = self.cache[key]['freq'], self.cache[key]['value']
        del self.freq[freq][key]
        if not self.freq[self.least_freq]:
            self.least_freq += 1
        self.cache[key] = {'freq': freq + 1, 'value': new_v or v}
        self.freq[freq + 1][key] = new_v or v
    
    def get(self, key):
        if key in self.cache:
            self._update(key)
            return self.cache[key]['value']
        return -1
    
    def put(self, key, value):
        if key in self.cache:
            self._update(key, value)
            return
        self.cache[key] = {'freq': 1, 'value': value}
        self.freq[1][key] = value
        if len(self.cache) > self.k:
            self._evict()
        self.least_freq = 1
