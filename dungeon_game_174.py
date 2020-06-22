'''
174. Dungeon Game
Hard

The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

 

Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

-2 (K)	-3	3
-5	-10	1
10	30	-5 (P)
 

Note:

The knight's health has no upper bound.
Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.

https://leetcode.com/problems/dungeon-game/
'''
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        dp = [[float("inf")]*(len(dungeon[0])+1) for _ in range(len(dungeon)+1)]
        dp[len(dungeon)-1][len(dungeon[0])], dp[len(dungeon)][len(dungeon[0])-1] = 1, 1
        for i in range(len(dungeon)-1,-1,-1):
            for j in range(len(dungeon[0])-1,-1,-1):
                dp[i][j] = max(min(dp[i+1][j],dp[i][j+1])-dungeon[i][j],1)
        return dp[0][0]
        # retVal = dungeon[0][0]
        # i, j = 0, 0
        # while i + 1 < len(dungeon) and j + 1 < len(dungeon[0]):
        #     if dungeon[i+1][j] > dungeon[i][j+1]:
        #         i += 1
        #     else:
        #         j += 1
        #     retVal+=dungeon[i][j]
        #     print(retVal, i, j)
        # if retVal >= 0:
        #     return 0
        # return (retVal+1)*-1
