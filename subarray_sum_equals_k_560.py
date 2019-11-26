'''
560. Subarray Sum Equals K
Medium

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2

https://leetcode.com/problems/subarray-sum-equals-k/
'''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic, sumVal, retVal = {0:1}, 0, 0
        for i in range(len(nums)):
            sumVal += nums[i]
            if sumVal-k in dic:
                retVal += dic.get(sumVal-k)
            if sumVal in dic:
                dic[sumVal] += 1
            else:
                dic[sumVal] =1
        return retVal

	# Failed for [0,0,0,0,0,0] 0
        # sumVal, retVal = [], 0
        # for i in range(len(nums)):
        #     if i == 0:
        #         sumVal.append(nums[i])
        #         if nums[i] == k:
        #             retVal +=1
        #     else:
        #         sumVal.append(sumVal[-1]+nums[i])
        #         if sumVal[-1] == k or nums[i] == k:
        #             retVal += 1
        #         elif  nums[i] < k and sumVal[-1] < k:
        #             continue
        #         else:
        #             for a in range(i,-1,-1):
        #                 if sumVal[-1] - sumVal[a] == k:
        #                     retVal +=1
        #                     break
        # return retVal
