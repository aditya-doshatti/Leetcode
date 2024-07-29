'''
1395. Count Number of Teams

Medium

There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

 

Example 1:

Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 

https://leetcode.com/problems/count-number-of-teams/description
'''
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        retVal = 0
        for j in range(n):
            leftLess = leftGreater = rightLess = rightGreater = 0
            for i in range(j):
                if rating[i] < rating[j]:
                    leftLess += 1
                elif rating[i] > rating[j]:
                    leftGreater += 1
            for k in range(j + 1, n):
                if rating[k] < rating[j]:
                    rightLess += 1
                elif rating[k] > rating[j]:
                    rightGreater += 1
            retVal += leftLess * rightGreater + leftGreater * rightLess
        return retVal
        '''
        TLE 62/72
        retVal = 0
        for i in range(len(rating) - 2):
            for j in range(i + 1, len(rating) - 1):
                for k in range(j + 1, len(rating)):
                    if rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k]:
                        retVal += 1
        return retVal
        '''
