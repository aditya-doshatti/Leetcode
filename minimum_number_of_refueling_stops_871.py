'''
871. Minimum Number of Refueling Stops
Hard

A car travels from a starting position to a destination which is target miles east of the starting position.

Along the way, there are gas stations.  Each station[i] represents a gas station that is station[i][0] miles east of the starting position, and has station[i][1] liters of gas.

The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it.  It uses 1 liter of gas per 1 mile that it drives.

When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.

What is the least number of refueling stops the car must make in order to reach its destination?  If it cannot reach the destination, return -1.

Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there.  If the car reaches the destination with 0 fuel left, it is still considered to have arrived.

 

Example 1:

Input: target = 1, startFuel = 1, stations = []
Output: 0
Explanation: We can reach the target without refueling.

https://leetcode.com/problems/minimum-number-of-refueling-stops/
'''
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        heap = []
        retVal, prevStation = 0, 0
        stations.append([target, float('inf')])
        curr = startFuel
        for i in range(len(stations)):
            curr -= (stations[i][0] - prevStation)
            while heap and curr < 0:
                curr += -heapq.heappop(heap)
                retVal +=1
            if curr < 0:
                return -1
            heapq.heappush(heap, -stations[i][1])
            prevStation = stations[i][0]
        return retVal

        # DP is slower than Heap
        # dp = [startFuel] + [0] * len(stations)
        # for i, station in enumerate(stations):
        #     for j in range(i, -1, -1):
        #         if dp[j] >= station[0]:
        #             dp[j+1] = max(dp[j+1], dp[j] + station[1])
        # for i, d in enumerate(dp):
        #     if d >= target: return i
        # return -1
        
        # Logic passed 50% test cases
        # totalF, fuellist = startFuel, []
        # if startFuel >= target:
        #     return 0
        # if not stations or startFuel < stations[0][0]:
        #     return -1
        # for i in range(len(stations)):
        #     totalF += stations[i][1]
        #     fuellist.append(stations[i][1])
        # balance = totalF-target
        # if balance < 0:
        #     return -1
        # #print(fuellist)
        # for i,f in enumerate(fuellist[::-1]):
        #     balance -= f
        #     print(balance, i)
        #     if balance < 0:
        #         return len(fuellist[i:])
