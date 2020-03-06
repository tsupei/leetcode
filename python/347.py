class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        sorted_nums = sorted(list(count.items()), key=lambda x: x[1], reverse=True)
        k_freq = [x[0] for x in sorted_nums[:k]]
        return k_freq
