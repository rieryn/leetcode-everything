class MedianFinder:
    import heapq

    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.low = []
        self.high = []

    def addNum(self, num: int) -> None:
        if len(self.low) == 0:
            heapq.heappush(self.low, -num)
            return
        if num <= -self.low[0]:
            heapq.heappush(self.low, -num)
        else:
            heapq.heappush(self.high, num)
        if len(self.low) - len(self.high) == 2:
            heapq.heappush(self.high, -1*(heapq.heappop(self.low)))
        elif len(self.low) - len(self.high) == -2:
            heapq.heappush(self.low, -1*(heapq.heappop(self.high)))

    def findMedian(self) -> float:
        if len(self.low) == len(self.high):
            return ((self.high[0]-self.low[0])/2)
        return -float(self.low[0]) if len(self.low) > len(self.high) else float(self.high[0])

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()