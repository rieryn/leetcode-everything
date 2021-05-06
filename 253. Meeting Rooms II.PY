class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        minr = sorted(intervals, key=lambda x:x[0])
        end = sorted(intervals, key=lambda x:x[1])
        print(minr)
        print(end)
        count = 0
        idx = 0
        for i in range(len(minr)):
            print(minr[i][0])
            print(end[idx][1])
            if minr[i][0]>=end[idx][1]:
                count -=1
                idx+=1
            count +=1
        return count