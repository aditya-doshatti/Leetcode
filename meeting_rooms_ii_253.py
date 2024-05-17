'''
253. Meeting Rooms II

Medium

Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

 

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

https://leetcode.com/problems/meeting-rooms-ii/description/
'''
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        roomCount, roomMap = 0, dict()
        intervals = sorted(intervals, key = lambda x:x[0])
        for interval in intervals:
            found = False
            start, end = interval[0], interval[1]
            for k,v in roomMap.items():
                if roomMap[k] <= start:
                    roomMap[k] = end
                    found = True
                    break
            if not found:
                roomMap[roomCount] = end
                roomCount += 1
            # print(roomMap)
        return roomCount
        '''
        Wrong answer 68/79
        roomCount, doneIdx = 0, set()
        intervals = sorted(intervals, key = lambda x:x[1], reverse=True)
        for i, interval in enumerate(intervals):
            if i not in doneIdx:
                start = interval[0]
                end = interval[1]
                j = i + 1
                while j < len(intervals):
                    if not start < intervals[j][0] < end and not start < intervals[j][1] < end:
                        doneIdx.add(j)
                    j += 1
                doneIdx.add(i)
                roomCount += 1
        return roomCount
        '''
