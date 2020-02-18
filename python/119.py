class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex < 0:
            return []
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        if rowIndex == 2:
            return [1,2,1]
        last = self.getRow(rowIndex-1)
        cur = [1]
        for i in range(len(last)-1):
            cur.append(last[i] + last[i+1])
        cur.append(1)
        return cur
