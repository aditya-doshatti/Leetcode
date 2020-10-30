'''
849. Maximize Distance to Closest Person
Medium

You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to the closest person.

 

Example 1:


Input: seats = [1,0,0,0,1,0,1]
Output: 2
Explanation: 
If Alex sits in the second open seat (i.e. seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.

https://leetcode.com/problems/maximize-distance-to-closest-person/
'''
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        emptyCount, maxDist = 0,0
        onebef = False
        for i in range(len(seats)):
            if seats[i] == 0:
                emptyCount += 1
            if seats[i] == 1:
                if onebef:
                    if emptyCount % 2:
                        if maxDist < int(emptyCount/2) + 1:
                            maxDist = int(emptyCount/2) + 1
                    else:
                        if maxDist < int(emptyCount/2):
                            maxDist = int(emptyCount/2)
                else:
                    maxDist = max(maxDist, emptyCount)
                onebef = True
                emptyCount = 0
        if emptyCount > maxDist:
            return emptyCount
        else:
            return maxDist
