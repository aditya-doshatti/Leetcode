'''
1001. Grid Illumination
Hard

On a N x N grid of cells, each cell (x, y) with 0 <= x < N and 0 <= y < N has a lamp.

Initially, some number of lamps are on.  lamps[i] tells us the location of the i-th lamp that is on.  Each lamp that is on illuminates every square on its x-axis, y-axis, and both diagonals (similar to a Queen in chess).

For the i-th query queries[i] = (x, y), the answer to the query is 1 if the cell (x, y) is illuminated, else 0.

After each query (x, y) [in the order given by queries], we turn off any lamps that are at cell (x, y) or are adjacent 8-directionally (ie., share a corner or edge with cell (x, y).)

Return an array of answers.  Each value answer[i] should be equal to the answer of the i-th query queries[i].

 

Example 1:

Input: N = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,0]]
Output: [1,0]
Explanation: 
Before performing the first query we have both lamps [0,0] and [4,4] on.
The grid representing which cells are lit looks like this, where [0,0] is the top left corner, and [4,4] is the bottom right corner:
1 1 1 1 1
1 1 0 0 1
1 0 1 0 1
1 0 0 1 1
1 1 1 1 1
Then the query at [1, 1] returns 1 because the cell is lit.  After this query, the lamp at [0, 0] turns off, and the grid now looks like this:
1 0 0 0 1
0 1 0 0 1
0 0 1 0 1
0 0 0 1 1
1 1 1 1 1
Before performing the second query we have only the lamp [4,4] on.  Now the query at [1,0] returns 0, because the cell is no longer lit.

https://leetcode.com/problems/grid-illumination/
'''
class Solution:
    def gridIllumination(self, N: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        retVal = []
        for q in queries:
            #print(lamps)
            if self.checkDiag(N, lamps, q) or self.checkAntiDiag(N, lamps, q) or self.checkRowCol(N, lamps, q):
                retVal.append(1)
            else:
                retVal.append(0)
            self.turnOff(N, lamps, q)
        return retVal
    
    def checkDiag(self, N, lamps, q):
        val = min(q[0], q[1])
        i,j = q[0]-val, q[1]-val
        while i < N and j < N:
            if [i,j] in lamps:
                return True
            i+=1
            j+=1
        else:
            return False
    
    def checkAntiDiag(self, N, lamps, q):
        i, j = 0 , q[1]+q[0]
        while i < N:
            if j < N:
                if [i,j] in lamps:
                    return True
            i += 1
            j -= 1
        else:
            return False

    def checkRowCol(self, N, lamps, q):
        for lamp in lamps:
            if lamp[0] == q[0] or lamp[1] == q[1]:
                return True
        return False

    def turnOff(self, N, lamps, q):
        i = 0
        while i < len(lamps):
            lamp = lamps[i]
            #print(lamp, i, q)
            if lamp[0] == q[0] or lamp[0]-1 == q[0] or lamp[0]+1 == q[0]:
                if lamp[1] == q[1]  or lamp[1]-1 == q[1] or lamp[1]+1 == q[1]:
                    lamps.pop(i) 
                    i -=1
            i +=1        
