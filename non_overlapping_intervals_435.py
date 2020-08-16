'''
435. Non-overlapping Intervals
Medium

Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

 

Example 1:

Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.

https://leetcode.com/problems/non-overlapping-intervals/
'''
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        count =  1
        if len(intervals) == 0: 
            return 0
        curr = intervals[0]
        for i in range(len(intervals)):
            if curr[1] <= intervals[i][0]:
                count += 1
                curr = intervals[i]
        return len(intervals) - count   
