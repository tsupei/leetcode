class Solution(object):
    def arr_combine(self, arr, k):
        if k == 1:
            return [[e] for e in arr]
        if len(arr) == 1:
            return [arr]

        ans = []
        for i in range(len(arr)-k+1):
            print(arr[:i] + arr[i+1:])
            ans.extend([ [ arr[i] ] + sub for sub in self.arr_combine(arr[i+1:], k-1)])
        return ans     
    
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k > n:
            return []
        return self.arr_combine(list(range(1,n+1)), k)

if __name__ == "__main__":
    sol = Solution()
    ans = sol.combine(5,3)
    print(ans)