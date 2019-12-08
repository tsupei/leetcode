class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        red = 0
        white = 0
        blue = 0
        for num in nums:
            if num == 0:
                red += 1
            elif num == 1:
                white += 1
            else:
                blue += 1
        for i in range(red):
            nums[i] = 0
        for i in range(red, red+white):
            nums[i] = 1
        for i in range(red+white, red+white+blue):
            nums[i] = 2

        

if __name__ == "__main__":
    sol = Solution()
    nums = []
    sol.sortColors(nums)
    print(nums)