class Solution(object):
    def binary_search(self, arr, target, offset):
        if not arr:
            return offset
        mid = len(arr) // 2
        if target < arr[mid]:
            return self.binary_search(arr[:mid], target, offset)
        if target > arr[mid]:
            return self.binary_search(arr[mid+1:], target, offset+mid+1)
        if target == arr[mid]:
            return mid + offset

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
        
        m = len(matrix)
        n = len(matrix[0])

        m_idx = self.binary_search([matrix[i][n-1] for i in range(m)], target , 0)
        if m_idx < m:
            n_idx = self.binary_search(matrix[m_idx], target, 0)
            if n_idx < n:
                if matrix[m_idx][n_idx] == target:
                    return True
        return False

# 1,2,3,5,6
# offset=2, [5,6]
# offset=2, [5]


if __name__ == "__main__":
    sol = Solution()
    arr = [7,20,50]
    target = 3
    # a = sol.binary_search(arr, target, 0)
    # print(a)

    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]

    target = 3
    a = sol.searchMatrix(matrix, target)
    print(a)
