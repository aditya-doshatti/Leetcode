'''
713. Subarray Product Less Than K
Medium

Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

https://leetcode.com/problems/subarray-product-less-than-k/
'''
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        i,j, retVal, curr = 0, 0, 0, 1
        while j < len(nums):
            curr *= nums[j]
            while curr >= k and i <=j:
                curr/=nums[i]
                i += 1
            retVal += j -i + 1
            j +=1
        return retVal

        # i,j, retVal, curr = 0, 0, 0, 0
        # while j < len(nums):
        #     if nums[j] < k:
        #         if curr !=0:
        #             if curr*nums[j] < k:
        #                 curr *= nums[j]
        #             else:
        #                 while i< j and curr*nums[j] >= k:
        #                     curr/=nums[i]
        #                     i += 1
        #                 curr *= nums[j]
        #         else:
        #             curr = nums[j]
        #         retVal = retVal + (j-i) + 1
        #     j +=1
        # return retVal
