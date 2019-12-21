def rrange(num):
        num -= 1
        while num >= 0:
            yield num
            num -= 1

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        ptr1 = m-1
        ptr2 = n-1
        for i in rrange(m+n):
            print(i, ptr1, ptr2)
            if ptr1 < 0:
                nums1[i] = nums2[ptr2]
                ptr2 -= 1
                continue
            elif ptr2 < 0:
                nums1[i] = nums1[ptr1]
                ptr1 -= 1
                continue

            if nums1[ptr1] > nums2[ptr2]:
                nums1[i] = nums1[ptr1]
                ptr1 -= 1
            else:
                nums1[i] = nums2[ptr2]
                ptr2 -= 1

if __name__ == "__main__":
    sol = Solution()
    nums1 = [0]
    nums2 = [1]
    sol.merge(nums1, 0, nums2, 1)
    print(nums1)
        