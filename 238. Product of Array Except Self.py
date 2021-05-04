class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        dp = []
        ans = []
        prod = 1
        has0 = 0
        hasnum = False
        for i in nums:
            if i == 0:
                has0 +=1
                continue
            prod *= i
        for i in nums:
            if has0 >= 2:
                ans.append(0)
            elif i == 0:
                ans.append(prod)
            elif has0 == 1:
                ans.append(0)
            else:
                ans.append(prod//i)
        return ans