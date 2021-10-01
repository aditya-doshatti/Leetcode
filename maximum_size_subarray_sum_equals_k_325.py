'''
325. Maximum Size Subarray Sum Equals k
Medium

Given an integer array nums and an integer k, return the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

 

Example 1:

Input: nums = [1,-1,5,-2,3], k = 3
Output: 4
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.

https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/
'''
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        sumVal, retVal = 0, 0
        dic = {}
        for i,num in enumerate(nums):
            # print(i, num, sumVal, dic)
            sumVal += num
            if sumVal == k:
                retVal = i +1
            if sumVal - k in dic.keys():
                retVal = max(retVal, i-dic[sumVal - k])
            if sumVal not in dic:
                dic[sumVal] = i
        return retVal
