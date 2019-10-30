class Solution(object):
    def binary_search(self, nums, target, offset):
        print(nums)
        if not nums:
            return offset 
        mid = len(nums) // 2
        if nums[mid] < target:
            return self.binary_search(nums[mid+1:], target, offset+mid+1)
        elif nums[mid] > target:
            return self.binary_search(nums[:mid], target, offset)
        else:
            return offset + mid
    
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.binary_search(nums,target,0)
if __name__ == "__main__":
    sol = Solution()
    ans = sol.searchInsert([1,3,5,6], 2)
    print(ans)