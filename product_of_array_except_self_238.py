'''
238. Product of Array Except Self
Medium

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

https://leetcode.com/problems/product-of-array-except-self/
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        retVal = [1] * len(nums)
        for i in range(1,len(nums)):
            retVal[i] = nums[i-1] * retVal[i-1]
        remaining = 1
        for i in range(len(nums)-1, -1, -1):
            retVal[i] = retVal[i] * remaining
            remaining *= nums[i]
        return retVal
        # Using division
        # retVal, product, zeroCount = [], 1, 0
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         product *= nums[i]
        #     else:
        #         zeroCount += 1
        # if zeroCount > 1:
        #     retVal = [0] * len(nums)
        # else:
        #     for i in range(len(nums)):
        #         if not zeroCount:
        #             retVal.append(product//nums[i])
        #         elif nums[i] == 0:
        #             retVal.append(product)
        #         else:
        #             retVal.append(0)
        # return retVal
