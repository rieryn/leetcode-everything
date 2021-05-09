class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        prev = None
        for i in range(len(nums)-1):
            if nums[i] == prev:
                continue
            print(nums[i])
            prev = nums[i]
            low = i+1
            high = len(nums)-1
            while low<high:
                if (nums[low]+nums[high]) == -nums[i]:
                    res.append((nums[i],nums[low],nums[high]))
                    prevlow = nums[low]
                    low +=1
                    high -=1
                    while low<high and nums[low] == prevlow:
                        low +=1
                elif (nums[low]+nums[high]) > -nums[i]:
                    high -=1
                else:
                    prevlow = nums[low]
                    low+=1
                    while low<high and nums[low] == prevlow:
                        low +=1
        return res
            