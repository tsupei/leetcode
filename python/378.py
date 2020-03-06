class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix:
            return None
        n = len(matrix)
        ptrs = [0] * n
        while True:
            # print(k)
            # print(ptrs)
            min_val = matrix[n-1][n-1]
            min_idx = n-1
            for idx, ptr in enumerate(ptrs):
                if ptr >= n:
                    continue
                if matrix[idx][ptr] < min_val:
                    min_val = matrix[idx][ptr]
                    min_idx = idx
            k -= 1
            if k == 0:
                return min_val
            ptrs[min_idx] += 1
        
