class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # intervals are sorted. no need to sort
        nintervals = []
        cur = 0
        while cur < len(intervals):
            ptr = 0
            upper_bound = intervals[cur][1]
            while cur+ptr+1 < len(intervals) and upper_bound >= intervals[cur+ptr+1][0]:
                upper_bound = upper_bound if intervals[cur+ptr+1][1] < upper_bound else intervals[cur+ptr+1][1]
                ptr += 1
            nintervals.append([intervals[cur][0], upper_bound])
            cur = cur+ptr+1
        return nintervals

    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        insert_idx = len(intervals)
        for idx in range(len(intervals)):
            lower_bound = intervals[idx][0]
            if newInterval[0] < lower_bound:
                insert_idx = idx
                break
        intervals.insert(insert_idx, newInterval)
        return self.merge(intervals)
if __name__ == "__main__":
    sol = Solution()
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    a = sol.insert(intervals, [4,8])
    print(a)





