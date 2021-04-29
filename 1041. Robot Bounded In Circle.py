class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dir = 0
        dis = {0: 0, 1: 0, 2: 0, 3: 0}
        for i in instructions:
            if i == 'G':
                dis[dir] = dis[dir] + 1
            if i == 'L':
                dir = (dir + 1)%4
            if i == 'R':
                dir = (dir -1)%4
        if dis[0]-dis[2] == 0 and dis[1]-dis[3] == 0:
            return True
        if dir !=0:
            return True
        return False