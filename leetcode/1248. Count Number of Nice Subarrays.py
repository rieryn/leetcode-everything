class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = {0:0}
        cnt = 0
        odd = 0
        for i in range(0, len(nums)):
            res[odd] += 1
            if nums[i] & 1:
                odd +=1
                res[odd] =0
            if odd >=k:
                cnt += res[odd-k]
        return cnt


