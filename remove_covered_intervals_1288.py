'''
1288. Remove Covered Intervals
Medium

Given a list of intervals, remove all intervals that are covered by another interval in the list.

Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.

After doing so, return the number of remaining intervals.

 

Example 1:

Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.

https://leetcode.com/problems/remove-covered-intervals/
'''
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <=1:
            return len(intervals)
        intervals = sorted(intervals, key=lambda k: (k[0],-k[1]))
        maxDone, retVal = intervals[0][1], 1
        for i in range(1,len(intervals)):
            if intervals[i][0] > maxDone or intervals[i][1]  > maxDone:
                retVal +=1
            maxDone = max(maxDone, intervals[i][1])
        return retVal
