class Solution(object):
    def bs(self, nums, target, offset):
        if not nums:
            return False
        mid = len(nums) // 2
        if nums[mid] > target:
            return self.bs(nums[:mid], target, offset)
        elif nums[mid] < target:
            return self.bs(nums[mid+1:], target, offset+mid+1)
        else:
            return True

    def find_pivot(self, nums, offset):
        mid = len(nums) // 2
        if not nums:
            return offset
        if len(nums) == 1:
            return offset
        if len(nums) == 2:
            if nums[0] <= nums[1]:
                return offset
            else:
                return offset+1
        if nums[mid] < nums[mid-1] and nums[mid] <= nums[mid+1]:
            return mid+offset
        if nums[mid] > nums[-1]:
            return self.find_pivot(nums[mid+1:],offset+mid+1)
        if nums[mid] < nums[0]:
            return self.find_pivot(nums[:mid], offset)
        return offset

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                return self.bs(nums[i:] + nums[:i], target, 0)
        return self.bs(nums, target, 0)

        
if __name__ == "__main__":
    sol = Solution()
    nums = [1,1,1,3, 1]
    target = 3
    ans = sol.search(nums, 3)
    print(ans)