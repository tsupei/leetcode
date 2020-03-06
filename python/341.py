# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        # 拆開List
        ptr = 0
        while True:
            if ptr >= len(nestedList):
                break
            while not nestedList[ptr].isInteger():
                if not nestedList[ptr].getList():
                    nestedList = nestedList[:ptr] + nestedList[ptr+1:]
                else:
                    nestedList = nestedList[:ptr] + nestedList[ptr].getList() + nestedList[ptr+1:]
                if ptr >= len(nestedList):
                    break
            ptr += 1
        self.ptr = 0
        self.nl = nestedList
        

    def next(self):
        """
        :rtype: int
        """
        val = self.nl[self.ptr]
        self.ptr += 1
        return val
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.ptr < len(self.nl):
            return True
        return False
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
