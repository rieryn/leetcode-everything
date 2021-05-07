class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        
        dp = [[0] + [float('inf')] * n for _ in range(d + 1)]
        
        for i in range(1, d + 1):
            for j in range(i, n + 1):
                maxd = 0
                for k in range(j, i - 1, -1):
                    current = max(maxd, jobDifficulty[k - 1])
                    dp[i][j] = min(dp[i][j], maxd + dp[i - 1][k - 1])
        return dp[-1][-1]

brute force:
for a day, we can put i to j jobs
for the next we can put j-i to j jobs
and so on to exhaustion

subproblem is jobs in days, recurse with alljobs - jobs and alldays - days
dp[i][j] is min difficulty of j jobs in i days

at day, with j jobs taken, take jobs from j to end of list
difficulty of that day is max of j to end of list  

add prev calc for days with j jobs taken
for day [i], we can take i to j jobs, 

for each day, the min difficulty is max difficulty for that day, plus the difficulty of other days

ok so clearly,
cases:
for day i with j jobs:
    take k to j jobs
    take k+1 to j jobs
    etc.

max difficulty is:
    max of k to j jobs + day i-1 with k jobs

then for day i with j jobs:
min difficulty is:
    min of all k..j to j jobs

the state eqn is therefores
dp[i][j]= min(
    dp[i-1][k-1] + max(k:j)
    dp[i-1][k+0] + max(k+1:j)
    ...
    from i<k<j; k++
)

the minimum of k is i, because going past i means the prev days don't have enough jobs
