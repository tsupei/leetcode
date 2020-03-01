class Node(object):
    def __init__(self, x):
        self.val = x
        self.children = []
        self.leaf = False
    
    def add(self, x):
        self.children.append(x)

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node("")
        
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        cur = self.root
        ptr = 0
        while ptr < len(word):
            for child in cur.children:
                if word[ptr] == child.val:
                    cur = child
                    ptr += 1
                    break
            else:
                node = Node(word[ptr])
                cur.add(node)
                ptr += 1
                cur = node
        cur.leaf = True
        
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        ptr = 0
        for i in range(len(word)):
            for child in cur.children:
                if word[i] == child.val:
                    cur = child
                    break
            else:
                return False
        if not cur.leaf:
            return False
        return True

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        ptr = 0
        for i in range(len(prefix)):
            for child in cur.children:
                if prefix[i] == child.val:
                    cur = child
                    break
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
