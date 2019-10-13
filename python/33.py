class Solution(object):
    def binary_search(self, nums, target, offset):
        #print(nums, offset)
        if not nums:
            return -1
        mid = int(len(nums)/2)
        if nums[mid] == target:
            return offset+mid
        elif nums[mid] > target:
            return self.binary_search(nums[:mid], target, offset)
        else:
            return self.binary_search(nums[mid+1:], target, offset+mid+1)

    def find_pivot(self, nums, offset):
        #print(nums, offset)
        mid = int(len(nums) / 2)
        if not nums:
            return offset
        if len(nums) == 1:
            return offset
        if len(nums) == 2:
            if nums[0] <= nums[1]:
                return offset
            else:
                return offset+1
        if nums[mid] < nums[mid-1] and nums[mid] < nums[mid+1]:
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
        :rtype: int
        """
        # find pivot
        pivot = self.find_pivot(nums,0)
        #print(pivot)
        #print(nums[pivot:]+nums[:pivot])
        idx = self.binary_search(nums[pivot:]+nums[:pivot], target, 0)
        if idx == -1:
            return idx
        return (idx + pivot)%len(nums)

if __name__ == "__main__":
    sol = Solution()
    nums = sol.search([1,3], 3)
    print(nums)