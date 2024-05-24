'''
568. Maximum Vacation Days

Hard

LeetCode wants to give one of its best employees the option to travel among n cities to collect algorithm problems. But all work and no play makes Jack a dull boy, you could take vacations in some particular cities and weeks. Your job is to schedule the traveling to maximize the number of vacation days you could take, but there are certain rules and restrictions you need to follow.

Rules and restrictions:

You can only travel among n cities, represented by indexes from 0 to n - 1. Initially, you are in the city indexed 0 on Monday.
The cities are connected by flights. The flights are represented as an n x n matrix (not necessarily symmetrical), called flights representing the airline status from the city i to the city j. If there is no flight from the city i to the city j, flights[i][j] == 0; Otherwise, flights[i][j] == 1. Also, flights[i][i] == 0 for all i.
You totally have k weeks (each week has seven days) to travel. You can only take flights at most once per day and can only take flights on each week's Monday morning. Since flight time is so short, we do not consider the impact of flight time.
For each city, you can only have restricted vacation days in different weeks, given an n x k matrix called days representing this relationship. For the value of days[i][j], it represents the maximum days you could take a vacation in the city i in the week j.
You could stay in a city beyond the number of vacation days, but you should work on the extra days, which will not be counted as vacation days.
If you fly from city A to city B and take the vacation on that day, the deduction towards vacation days will count towards the vacation days of city B in that week.
We do not consider the impact of flight hours on the calculation of vacation days.
Given the two matrices flights and days, return the maximum vacation days you could take during k weeks.

 

Example 1:

Input: flights = [[0,1,1],[1,0,1],[1,1,0]], days = [[1,3,1],[6,0,3],[3,3,3]]
Output: 12
Explanation:
One of the best strategies is:
1st week : fly from city 0 to city 1 on Monday, and play 6 days and work 1 day.
(Although you start at city 0, we could also fly to and start at other cities since it is Monday.)
2nd week : fly from city 1 to city 2 on Monday, and play 3 days and work 4 days.
3rd week : stay at city 2, and play 3 days and work 4 days.
Ans = 6 + 3 + 3 = 12.
https://leetcode.com/problems/maximum-vacation-days/description/
'''
class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        n, weeks, airports = len(flights), len(days[0]), defaultdict(list)
        for i in range(n):
            for j in range(n):
                if flights[i][j] == 1:
                    airports[i].append(j)
        @lru_cache(None)
        def dfs(i,j):
            if i >= n or j >= weeks:
                return 0
            retVal = float("-inf")
            retVal = max(retVal,days[i][j] + dfs(i,j+1))
            for destination in airports[i]:
                retVal = max(retVal,days[destination][j] + dfs(destination,j+1))
            return retVal
        return dfs(0,0)
        '''
        TLE 38/57
        airports = defaultdict(list)
        for i in range(len(flights)):
            for j in range(len(flights[i])):
                if flights[i][j] or i == j:
                    airports[i].append(j)
        retVal = 0
        for i in range(len(days)):
            if i == 0 or i in airports[0]:
                retVal = max(retVal, sum(days[i]))
        @lru_cache(None)
        def dfs(i, j, vacay):
            nonlocal retVal
            vacay += days[i][j]
            retVal = max(retVal, vacay)
            for a in range(len(days)):
                if a in airports[i]:
                    if j < len(days[0]) - 1:
                        dfs(a, j+1, vacay)
            vacay -= days[i][j]
        for next in airports[0]:
            dfs(next, 0, 0)
        return retVal
        '''
                    
