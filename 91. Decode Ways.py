class Solution:
    prev = ""
    ways = {}
    def numDecodings(self, s: str) -> int:
        prev = ""
        self.ways = {}
        return self.calcways(0,s)
            
    def calcways(self, i, s:str):

        if i == len(s):
            return 1
        if s[i] == '0':
            return 0
        if i == len(s)-1:
            return 1
        if i in self.ways:
            return self.ways[i]
        
        else:
            if int(s[i]+s[i+1])<=26:
                self.ways[i] = self.calcways(i+1,s)+self.calcways(i+2,s)
            else:
                self.ways[i]= self.calcways(i+1,s)
            return self.ways[i]
        
        
            