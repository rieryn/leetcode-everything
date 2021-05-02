class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        sum = 0
        prevl = 0
        prevr = 0
        while (left < right-1):
            if height[left]<height[right]:
                prevl = max(prevl,height[left])
                left +=1
                if prevl > height[left]:
                    sum = sum + prevl-height[left]
            if height[left]>= height[right]:
                prevr = max(prevr, height[right])
                right -=1
                if prevr>height[right]:
                    sum += prevr-height[right]
        return sum