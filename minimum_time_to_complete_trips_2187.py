'''
2187. Minimum Time to Complete Trips
Medium
1.1K
66
Companies
You are given an array time where time[i] denotes the time taken by the ith bus to complete one trip.

Each bus can make multiple trips successively; that is, the next trip can start immediately after completing the current trip. Also, each bus operates independently; that is, the trips of one bus do not influence the trips of any other bus.

You are also given an integer totalTrips, which denotes the number of trips all buses should make in total. Return the minimum time required for all buses to complete at least totalTrips trips.

 

Example 1:

Input: time = [1,2,3], totalTrips = 5
Output: 3
Explanation:
- At time t = 1, the number of trips completed by each bus are [1,0,0]. 
  The total number of trips completed is 1 + 0 + 0 = 1.
- At time t = 2, the number of trips completed by each bus are [2,1,0]. 
  The total number of trips completed is 2 + 1 + 0 = 3.
- At time t = 3, the number of trips completed by each bus are [3,1,1]. 
  The total number of trips completed is 3 + 1 + 1 = 5.
So the minimum time needed for all buses to complete at least 5 trips is 3.

https://leetcode.com/problems/minimum-time-to-complete-trips
'''
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int: 
        right = min(time) * totalTrips + 1 
        left = 0
        retVal = 0

        def isSmaller(answer: int) -> int:
            nonlocal retVal
            count = 0
            for i in time:
                count += answer // i # Total trips with time answer should be integer part of answer // i
            if count < totalTrips:
                return True # Since number of trips are less than required, left moves to mid
            elif count >= totalTrips:
                retVal = answer # stores the latest result. This is the minimum possible answer.
                return False # Since number of trips are greater/equal to required, right moves to mid

        while left < right-1: # Till Binary Search can continue. 
            mid = (left + right) // 2 # mid is the current expected time.
            status = isSmaller(mid) # The return values isSmaller function determines which pointer to move.
            if status:
                left = mid
            else:
                right = mid
                
        return retVal
