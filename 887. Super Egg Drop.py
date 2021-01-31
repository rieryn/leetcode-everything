class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = {}
        def f(K,N):
            if K ==1:
                return N
            if N == 0:
                return 0
            if (K,N) in dp:
                return dp[(K,N)]

            res = math.inf
            left, right = 1, N
            while left <= right:
                mid = (left+right)//2
                broke = f(K-1, mid-1)
                nobreak = f(K,N-mid)
                if broke>nobreak:
                    right = mid-1
                    res = min(res,(broke+1))
                if nobreak>= broke:
                    left = mid+1
                    res = min(res,(nobreak+1))

            dp[(K,N)] = res
            return res
        
        return f(K,N)