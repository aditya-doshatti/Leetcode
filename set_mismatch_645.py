'''
645. Set Mismatch
Easy

The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]

https://leetcode.com/problems/set-mismatch/
'''
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # val,retVal,sumVal = {},0,0
        # for i in nums:
        #     if val.get(i, None):
        #         retVal = i
        #     else:
        #         val[i] = 1
        #     sumVal += i
        # n = len(nums)
        # actSum = int((n*(n+1))/2)
        # diff = actSum - sumVal
        # #print(val, retVal, actSum, diff, sumVal)
        # return [retVal, retVal+diff]

        n = len(nums)
        actSum = int((n*(n+1))/2)
        setSum, listSum = sum(set(nums)), sum(nums)
        return [listSum-setSum, actSum - setSum]
