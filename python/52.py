class Solution(object):
    def place(self, num, record, chess):
        n = len(chess)
        if num >= n:
            return [chess]
        row = num
        ans = []
        for col in range(n):
            # print(n,num,col)
            # self.pm(chess)
            # self.pm(record)

            if record[row][col] == 0:
                cp_chess = [e[:] for e in chess]
                cp_record = [e[:] for e in record]
                cp_chess[row][col] = 'Q'

                for i in range(n):
                    cp_record[row][i] = 1
                for i in range(n):
                    cp_record[i][col] = 1
                for i in range(1,n):
                    if row+i<n and col+i<n:
                        cp_record[row+i][col+i] = 1
                    if row-i>=0 and col-i>=0:
                        cp_record[row-i][col-i] = 1
                for i in range(1,n):
                    if row+i<n and col-i>=0:
                        cp_record[row+i][col-i] = 1
                    if row-i>=0 and col+i<n:
                        cp_record[row-i][col+i] = 1
                ans.extend(self.place(num+1, cp_record, cp_chess))
        return ans

    def pm(self, chess):
        for row in chess:
            print(row)
        print('\n')

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        # There must one queen in the first row
        record = [[0 for i in range(n)] for j in range(n)]
        chess = [['.' for i in range(n)] for j in range(n)]
        ans = self.place(0, record, chess)
        ans_ = []
        for ch in ans:
            ch_ = []
            for row in ch:
                ch_.append("".join(row))
            ans_.append(ch_)
        return len(ans_)


if __name__ == "__main__":
    sol = Solution()
    ans = sol.solveNQueens(5)
    print(ans)

