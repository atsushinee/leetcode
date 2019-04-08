class Solution:
    def minFallingPathSum(self, A) -> int:
        dp = A[:]
        N = len(A)
        if N == 1:
            return A[0][0]
        for i in range(1, N):
            for j in range(N):
                if j == 0:
                    dp[i][j] = A[i][j] + min(dp[i-1][j], dp[i-1][j+1])
                else:
                    if j == N-1:
                        dp[i][j] = A[i][j] + min(dp[i-1][j], dp[i-1][j-1])
                    else:
                        dp[i][j] = A[i][j] + \
                            min(min(dp[i-1][j-1], dp[i-1][j]), dp[i-1][j+1])

        val = 100
        for i in range(N):
            val = min(dp[N-1][i], val)
        return val


if __name__ == "__main__":
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(Solution().minFallingPathSum(A))
