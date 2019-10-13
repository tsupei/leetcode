class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # move from the last
        # 
        # check if there are bigger number behind
        find = False
        for idx in range(len(nums)):
            idx = len(nums) - idx - 1
            max_num = nums[idx]
            target = nums[idx]
            bigger_min = None
            bigger_min_idx = -1
            for j in range(idx, len(nums)):
                if not bigger_min:
                    if nums[j] > target:
                        bigger_min = nums[j]
                        bigger_min_idx = j
                else:
                    if nums[j] > target and nums[j] < bigger_min:
                        bigger_min = nums[j]
                        bigger_min_idx = j

            if bigger_min:
                tmp = nums[idx]
                nums[idx] = bigger_min
                nums[bigger_min_idx] = tmp
                nums[idx+1:] = sorted(nums[idx+1:])
                find = True
                break
        if find:
            return nums
        else:
            # nums = nums[::-1]
            nums.reverse()
            return nums

if __name__ == "__main__":
    sol = Solution()
    nums = sol.nextPermutation([3,2,1])
    print(nums)