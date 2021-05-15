class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ordermap = {}
        for k, v in enumerate(order):
            ordermap[v] = k
        prev = []
        
        for word in words:
            val = []
            for letter in word:
                val.append(ordermap[letter])
            print(prev)
            for i in range(len(prev)):
                if i >= len(val): return False
                if prev[i] != val[i]:
                    if prev[i] > val[i]: return False
                    break
            prev = val
        return True