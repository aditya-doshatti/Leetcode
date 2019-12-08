'''
56. Merge Intervals
Medium

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

https://leetcode.com/problems/merge-intervals/
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        retVal = []
        for i in intervals:
            if not retVal or retVal[-1][1] < i[0]:
                retVal.append(i)
            else:
                retVal[-1][1] = max(retVal[-1][1], i[1])
        return retVal
        # retVal = []
        # for val in intervals:
        #     updated = False
        #     if len(retVal) == 0:
        #         retVal.append(val)
        #     else:
        #         for i in range(len(retVal)):
        #             if retVal[i][1] >= val[0] >= retVal[i][0]:
        #                 retVal[i][1] = max(retVal[i][1], val[1])
        #                 retVal[i][0] = min(retVal[i][0], val[0])
        #                 updated = True
        #             elif val[1] >= retVal[i][0] >= val[0]:
        #                 retVal[i][1] = max(retVal[i][1], val[1])
        #                 retVal[i][0] = min(retVal[i][0], val[0])
        #                 updated = True
        #         if not updated:
        #             retVal.append(val)
        # finalRetval = []
        # while retVal:
        #     k = retVal.pop()
        #     if k not in finalRetval:
        #         finalRetval.append(k)
        # return finalRetval
