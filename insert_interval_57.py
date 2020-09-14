'''
57. Insert Interval
Hard

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

https://leetcode.com/problems/insert-interval/
'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        while i < len(intervals) and newInterval[0] > intervals[i][1]:
            result += intervals[i],
            i += 1
        thisInterval = [0,0]
        while i < len(intervals) and newInterval[1] >= intervals[i][0]:
            thisInterval[0] = int(min(newInterval[0], intervals[i][0]))
            thisInterval[1] =  int(max(newInterval[1], intervals[i][1]))
            newInterval = thisInterval
            i += 1
        result += newInterval,
        result += intervals[i:]
        return result
