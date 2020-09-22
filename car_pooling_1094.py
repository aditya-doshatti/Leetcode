'''
1094. Car Pooling
Medium

You are driving a vehicle that has capacity empty seats initially available for passengers.  The vehicle only drives east (ie. it cannot turn around and drive west.)

Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains information about the i-th trip: the number of passengers that must be picked up, and the locations to pick them up and drop them off.  The locations are given as the number of kilometers due east from your vehicle's initial location.

Return true if and only if it is possible to pick up and drop off all passengers for all the given trips. 

 

Example 1:

Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false

https://leetcode.com/problems/car-pooling/
'''
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        count = [0] * 1000
        for passegers, start, end in trips:
            count[start] += passegers
            count[end] -= passegers
        total_passengers = 0
        for c in count:
            total_passengers += c
            if total_passengers > capacity: 
                return False
        return True
        # count = [0] * 1000
        # for i in range(len(trips)):
        #     for j in range(trips[i][1], trips[i][2]):
        #         count[j] += trips[i][0]
        #         if count[j] > capacity:
        #             return False
        # return True
