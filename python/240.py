class Solution(object):
    def bs(self, arr, target, offset):
        if not arr:
            return False
        mid = len(arr) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            return self.bs(arr[mid+1:], target, offset+mid+1)
        else:
            return self.bs(arr[:mid], target, offset)
        
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        if not matrix[0]:
            return False
#         e = len(matrix[0])
#         for i in range(len(matrix[0])):
#             if matrix[0][i] > target:
#                 e = i

#         s = 0
#         for i in range(len(matrix[0])):
#             if matrix[-1][i] >= target:
#                 s = i
#                 break
        for idx, arr in enumerate(matrix):
            if arr[0] <= target <= arr[-1]:
                if self.bs(arr, target, 0):
                    return True
        return False
