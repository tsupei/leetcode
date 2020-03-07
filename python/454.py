class Solution(object):       
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        cnt = 0
        
        n = len(A)
        # O(n^2)
        # AB = [A[i] + B[j] for i in range(n) for j in range(n)]
        # CD = [C[i] + D[j] for i in range(n) for j in range(n)]
        
        # O(n^2)
        count_AB = {}
        for numA in A:
            for numB in B:
                if numA+numB not in count_AB:
                    count_AB[numA+numB] = 1
                else:
                    count_AB[numA+numB] += 1
        
        count_CD = {}
        for numC in C:
            for numD in D:
                if numC+numD not in count_CD:
                    count_CD[numC+numD] = 1
                else:
                    count_CD[numC+numD] += 1
        # O(n^2)
        for num in count_AB:
            if -num in count_CD:
                cnt += count_AB[num] * count_CD[-num]
        return cnt
                        
