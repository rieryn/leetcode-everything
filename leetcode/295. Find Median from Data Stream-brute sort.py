class MedianFinder:
    arr = []
    left = 0
    right = 0
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []
        self.left = 0
        self.right = 0
        print("init")
        

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        if len(self.arr) % 2 == 0:
            self.left +=1
        else:
            self.right +=1
        if len(self.arr) == (2 or 1):
            print("2 or 1")
            self.left = 0
            self.right = 1
        if len(self.arr) == 3:
            self.left = 0
            self.right = 2
       
        self.arr.sort()

    def findMedian(self) -> float:
        if len(self.arr) == 0:
            return 0
        if len(self.arr) == 1:
            return self.arr[0]
        if len(self.arr) % 2 == 0:
            return (self.arr[self.left]+self.arr[self.right])/2
        return (self.arr[self.left+1])

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()