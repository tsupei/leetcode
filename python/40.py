class Solution(object):
    def combinationSum(self, candidates, target):
        cur = 0
        prev = None
        ans = []
        while cur < len(candidates):
            if prev or prev == 0:
                if candidates[cur] == candidates[prev]:
                    cur += 1
                    continue
            if target - candidates[cur] > 0:
                sub_anss = self.combinationSum(candidates[cur+1:], target-candidates[cur])
                for sub_ans in sub_anss:
                	sub_ans.append(candidates[cur])
                	ans.append(sub_ans)
            elif target - candidates[cur] == 0:
                ans.append([candidates[cur]])
            prev = cur
            cur += 1
        return ans

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        cur = 0
        prev = None
        ans = []
        while cur < len(candidates):
            if prev or prev == 0:
                if candidates[cur] == candidates[prev]:
                    cur += 1
                    continue
            if target - candidates[cur] > 0:
                sub_anss = self.combinationSum(candidates[cur+1:], target-candidates[cur])
                for sub_ans in sub_anss:
                	sub_ans.append(candidates[cur])
                	ans.append(sub_ans)
            elif target - candidates[cur] == 0:
                ans.append([candidates[cur]])
            prev = cur
            cur += 1
        return ans
        
if __name__ == "__main__":
    sol = Solution()
    candidates = [1,1,1,2,3]
    target = 4
    print(sol.combinationSum2(candidates, target))