# Bad Answer
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        for cand in candidates:
            if target - cand == 0:
                ans.append([cand])
                continue
            elif target - cand < 0:
                continue
            recs = self.combinationSum(candidates, target-cand)
            if recs:
                for rec in recs:
                    rec.insert(0,cand)
                    # check
                    for comb in ans:
                        cp = comb[:]
                        for e in rec:
                            if e not in cp:
                                # Pass
                                break
                            else:
                                cp.remove(e)
                        else:
                            if not cp:
                                # Fail
                                break
                    else:
                        ans.append(rec)

            print(target, ans, cand)

        return ans
if __name__ == "__main__":
    sol = Solution()
    candidates = [2,3,5,7]
    target = 8
    print(sol.combinationSum(candidates, target))

# [[3,3,3,3,3,3,3,3,3],[3,3,3,3,3,3,4,5],[3,3,3,3,3,3,9],[3,3,3,3,3,4,4,4],[3,3,3,3,3,4,8],[3,3,3,3,3,12],[3,3,3,3,5,5,5],[3,3,3,3,5,10],[3,3,3,4,4,5,5],[3,3,3,4,4,10],[3,3,3,4,5,9],[3,3,3,5,5,8],[3,3,3,8,10],[3,3,3,9,9],[3,3,4,4,4,4,5],[3,3,4,4,4,9],[3,3,4,4,5,8],[3,3,4,5,12],[3,3,4,8,9],[3,3,5,8,8],[3,3,9,12],[3,4,4,4,4,4,4],[3,4,4,4,4,8],[3,4,4,4,12],[3,4,4,8,8],[3,4,5,5,5,5],[3,4,5,5,10],[3,4,8,12],[3,4,10,10],[3,5,5,5,9],[3,5,9,10],[3,8,8,8],[3,12,12],[4,4,4,5,5,5],[4,4,4,5,10],[4,4,5,5,9],[4,4,9,10],[4,5,5,5,8],[4,5,8,10],[4,5,9,9],[5,5,5,12],[5,5,8,9],[5,10,12],[8,9,10],[9,9,9]]