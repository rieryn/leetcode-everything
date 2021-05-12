class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        lh = 0
        lv = 0
        prev = 0
        horizontalCuts = sorted(horizontalCuts) + [h]
        verticalCuts = sorted(verticalCuts) + [w]
        for i in horizontalCuts:
            lh = max(lh, i - prev)
            prev = i
        prev = 0
        for i in verticalCuts:
            lv = max(lv, i-prev)
            prev = i
        return lh*lv % (10**9+7)