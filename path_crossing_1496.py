'''
1496. Path Crossing
Easy

Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.

 

Example 1:


Input: path = "NES"
Output: false 
Explanation: Notice that the path doesn't cross any point more than once.

https://leetcode.com/problems/path-crossing/
'''
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set()
        dic = {'N':(0,1),'S':(0,-1),'E':(-1,0),'W':(1,0)}
        loc = (0,0)
        visited.add(loc)
        for char in path:
            x, y = loc[0], loc[1]
            x += dic[char][0]
            y += dic[char][1]
            loc = (x,y)
            if loc not in visited:
                visited.add(loc)
            else:
                return True
        return False
