'''
532. K-diff Pairs in an Array
Medium

Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

0 <= i, j < nums.length
i != j
a <= b
b - a == k
 

Example 1:

Input: nums = [3,1,4,1,5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.

https://leetcode.com/problems/k-diff-pairs-in-an-array/
'''
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        retVal = 0
        counter = collections.Counter(nums)
        
        for key in counter:
            if k > 0 and key + k in counter:
                retVal += 1
            elif k == 0 and counter[key] > 1:
                retVal += 1
        return retVal
        # lookup, retVal = [], 0
        # if k < 0:
        #     return 0
        # if k == 0:
        #     setVal = set(nums)
        #     for val in setVal:
        #         if nums.count(val) > 1:
        #             retVal += 1
        #     return retVal
        # for elem in nums:
        #     if elem in lookup:
        #         continue
        #     else:
        #         if elem + k in lookup:
        #             retVal += 1
        #         if elem - k in lookup:
        #             retVal += 1
        #         lookup.append(elem)
        # return retVal
