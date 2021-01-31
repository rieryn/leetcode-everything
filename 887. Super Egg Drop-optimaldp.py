class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[0]*(N+1) for _ in range(K+1)]
        m = 0
        while dp[K][m]<N:
            m+=1
            for i in range(1, K+1):
                dp[i][m] = dp[i][m-1]+dp[i-1][m-1]+1
        return m