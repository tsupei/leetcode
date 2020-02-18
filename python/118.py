class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]
        if numRows == 3:
            return [[1], [1,1], [1,2,1]]
        pascal = self.generate(numRows-1)
        last_row = pascal[-1]
        cur = [1]
        for i in range(len(last_row)-1):
            cur.append(last_row[i] + last_row[i+1])
        cur.append(1)
        pascal.append(cur)
        return pascal
