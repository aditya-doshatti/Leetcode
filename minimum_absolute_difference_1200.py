'''
1200. Minimum Absolute Difference
Easy

Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements. 

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr
 

Example 1:

Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.

https://leetcode.com/problems/minimum-absolute-difference/
'''
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mini, retVal = abs(arr[1] - arr[0]), [arr[0:2]]
        for i in range(2, len(arr)):
            diff = abs(arr[i] - arr[i - 1])
            if diff > mini:
                continue
            if diff < mini:
                mini, retVal = diff, list()
            retVal.append([arr[i - 1], arr[i]])
        return retVal
