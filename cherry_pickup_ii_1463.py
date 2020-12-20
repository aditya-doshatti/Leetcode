'''
1463. Cherry Pickup II
Hard
Given a rows x cols matrix grid representing a field of cherries. Each cell in grid represents the number of cherries that you can collect.

You have two robots that can collect cherries for you, Robot #1 is located at the top-left corner (0,0) , and Robot #2 is located at the top-right corner (0, cols-1) of the grid.

Return the maximum number of cherries collection using both robots  by following the rules below:

From a cell (i,j), robots can move to cell (i+1, j-1) , (i+1, j) or (i+1, j+1).
When any robot is passing through a cell, It picks it up all cherries, and the cell becomes an empty cell (0).
When both robots stay on the same cell, only one of them takes the cherries.
Both robots cannot move outside of the grid at any moment.
Both robots should reach the bottom row in the grid.
 

Example 1:



Input: grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
Output: 24
Explanation: Path of robot #1 and #2 are described in color green and blue respectively.
Cherries taken by Robot #1, (3 + 2 + 5 + 2) = 12.
Cherries taken by Robot #2, (1 + 5 + 5 + 1) = 12.
Total of cherries: 12 + 12 = 24.

https://leetcode.com/problems/cherry-pickup-ii/
'''
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        pos_cherry = {(0,n-1):grid[0][0]+grid[0][-1]}
        for i in range(1,m):
            new = {}
            for (x,y),val in pos_cherry.items():
                robot1 = [i for i in [x-1,x,x+1] if i>=0 and i<n]
                robot2 = [i for i in [y-1,y,y+1] if i>=0 and i<n]
                for a in robot1:
                    for b in robot2:
                        new_val = val + grid[i][a] + grid[i][b] * (a!=b)
                        if (a,b) not in new or new_val > new[(a,b)]:
                            new[(a,b)] = new_val
            pos_cherry = new
        return max(pos_cherry.values())
