class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.insert(0, 1)
        subarray = []
        offset = 0
        #print(nums)
        for i in range(1, len(nums)):
            if nums[i] == 0:
                subarray.append(nums[offset:i])
                subarray.append([1,0]) # 0 could sometime be the maximum value
                offset = i
                nums[i] = 1
            else:
                nums[i] = nums[i] * nums[i-1]
        subarray.append(nums[offset:len(nums)])
        for arr in subarray:
            arr.pop(0)
        subarray = filter(lambda x:x, subarray)

        print(subarray)
        max_val = None
        for arr in subarray:
            biggest = arr[-1]
            if biggest < 0:
                # find the maximum negative integer and maximum positive integer
                max_neg = None
                for val in arr[:-1]:
                    if val < 0 and (max_neg is None or val > max_neg):
                        max_neg = val
                        break
                max_pos = None
                for val in arr[::-1]:
                    if val > 0:
                        max_pos = val
                        break
                if not max_neg and not max_pos:
                    biggest = biggest
                elif not max_neg:
                    biggest = max_pos
                elif not max_pos:
                    biggest /= max_neg
                else:
                    biggest = max(biggest / max_neg, max_pos)
            if max_val is None:
                max_val = biggest
            else:
                if biggest > max_val:
                    max_val = biggest
        if max_val is None:
            return 0
        return max_val

if __name__ == "__main__":
    sol = Solution()
    nums = [-2, 0, 0, 0, -5, -1]
    ans = sol.maxProduct(nums)
    print(ans)
