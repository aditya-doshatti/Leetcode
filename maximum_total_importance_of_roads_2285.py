'''
2285. Maximum Total Importance of Roads

Medium

You are given an integer n denoting the number of cities in a country. The cities are numbered from 0 to n - 1.

You are also given a 2D integer array roads where roads[i] = [ai, bi] denotes that there exists a bidirectional road connecting cities ai and bi.

You need to assign each city with an integer value from 1 to n, where each value can only be used once. The importance of a road is then defined as the sum of the values of the two cities it connects.

Return the maximum total importance of all roads possible after assigning the values optimally.


Example 1:

Input: n = 5, roads = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]
Output: 43
Explanation: The figure above shows the country and the assigned values of [2,4,5,3,1].
- The road (0,1) has an importance of 2 + 4 = 6.
- The road (1,2) has an importance of 4 + 5 = 9.
- The road (2,3) has an importance of 5 + 3 = 8.
- The road (0,2) has an importance of 2 + 5 = 7.
- The road (1,3) has an importance of 4 + 3 = 7.
- The road (2,4) has an importance of 5 + 1 = 6.
The total importance of all roads is 6 + 9 + 8 + 7 + 7 + 6 = 43.
It can be shown that we cannot obtain a greater total importance than 43.

https://leetcode.com/problems/maximum-total-importance-of-roads/description
'''
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        roadArr = [0] * n
        for s, d in roads:
            roadArr[s] += 1
            roadArr[d] += 1
        roadArr.sort()
        retVal = 0
        for i in range(len(roadArr)):
            retVal += roadArr[i] * (i+1)
        return retVal
        '''
        This solution works but ^ is optimal
        roadMap = defaultdict(list)
        for s,d in roads:
            roadMap[s].append(d)
            roadMap[d].append(s)
        sortedMap = dict(sorted(roadMap.items(), key = lambda x:len(x[1]), reverse = True))
        valMap, num = {}, n
        for k,v in sortedMap.items():
            valMap[k] = num
            num -= 1
        retVal = 0
        for s,d in roads:
            retVal += (valMap[s] + valMap[d])
        return retVal
        '''
