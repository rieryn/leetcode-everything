class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        first = 0
        end = len(piles)-1
        res = 0
        piles.sort()
        while first<end:
            print(first)
            print(end)
            first +=1
            end -=1
            res += piles[end]
            end -=1
        return res