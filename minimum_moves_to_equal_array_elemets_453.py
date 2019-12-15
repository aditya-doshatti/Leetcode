'''
453. Minimum Moves to Equal Array Elements
Easy

Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.

Example:

Input:
[1,2,3]

Output:
3

Explanation:
Only three moves are needed (remember each move increments two elements):

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]

https://leetcode.com/problems/minimum-moves-to-equal-array-elements/
'''
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        i, retVal = len(nums)-1, 0
        while i > -1:
            retVal += (nums[i]-nums[0])
            i-=1
        return retVal
        # Brute Force
        # retVal = 0
        # if len(nums) <= 1:
        #     return retVal
        # while len(set(nums)) != 1:
        #     nums.sort()
        #     i =0
        #     while i < len(nums)-1:
        #         nums[i]+=1
        #         i+=1
        #     retVal+=1
        # return retVal
