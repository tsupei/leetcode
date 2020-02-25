class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.keys = {}
        self.values = [-1] * capacity
        self.history = []
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.keys:
            if key in self.history:
                self.history.remove(key)
                self.history.append(key)
            return self.values[self.keys[key]]
        return -1


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.keys:
            self.values[self.keys[key]] = value
            if key in self.history:
                self.history.remove(key)
                self.history.append(key)
            return
        if len(self.history) < self.capacity:
            kptr = len(self.history)
        else:
            lru_key = self.history.pop(0)
            kptr = self.keys[lru_key]
            del self.keys[lru_key]

        self.keys[key] = kptr
        self.values[kptr] = value
        self.history.append(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
