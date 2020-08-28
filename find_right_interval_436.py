'''
436. Find Right Interval
Medium

Given a set of intervals, for each of the interval i, check if there exists an interval j whose start point is bigger than or equal to the end point of the interval i, which can be called that j is on the "right" of i.

For any interval i, you need to store the minimum interval j's index, which means that the interval j has the minimum start point to build the "right" relationship for interval i. If the interval j doesn't exist, store -1 for the interval i. Finally, you need output the stored value of each interval as an array.

Note:

You may assume the interval's end point is always bigger than its start point.
You may assume none of these intervals have the same start point.
 

Example 1:

Input: [ [1,2] ]

Output: [-1]

Explanation: There is only one interval in the collection, so it outputs -1.

https://leetcode.com/problems/find-right-interval/
'''
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        if len(intervals) < 2:
            return [-1]
        dic, lst = {}, []
        for i, val in enumerate(intervals):
            dic[val[0]] = i
            lst.append(val[0])
        lst.sort()
        retVal = []
        for val in intervals:
            end = val[1]
            lo = 0
            hi = len(intervals)
            while lo < hi:
                mid = (lo + hi) // 2
                if lst[mid] < end:
                    lo = mid+1
                else:
                    hi = mid
            if lo == len(intervals):
                retVal.append(-1)
            else:
                retVal.append(dic[lst[lo]])
        return retVal
            
			
