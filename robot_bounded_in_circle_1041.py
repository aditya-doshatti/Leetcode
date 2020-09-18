'''
1041. Robot Bounded In Circle
Medium

On an infinite plane, a robot initially stands at (0, 0) and faces north.  The robot can receive one of three instructions:

"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degress to the right.
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

 

Example 1:

Input: "GGLLGG"
Output: true
Explanation: 
The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.

https://leetcode.com/problems/robot-bounded-in-circle/
'''
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        go = {'N':(0,1), 'S':(0,-1), 'W':(-1,0), 'E':(1,0)}
        left = {'N':'W', 'W':'S', 'S':'E', 'E':'N'}
        right = {'N':'E', 'E':'S', 'S':'W', 'W':'N'}
        current = [0, 0]
        direction = 'N'
        
        for i in instructions:
            if i == 'G':
                x, y = go[direction]
                current[0] += x
                current[1] += y
            elif i == 'L':
                direction = left[direction]
            else:
                direction = right[direction]
        
        if current == [0,0] or direction != 'N':
            return True
        else:
            return False
