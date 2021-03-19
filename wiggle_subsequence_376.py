'''
376. Wiggle Subsequence
Medium

Given an integer array nums, return the length of the longest wiggle sequence.

A wiggle sequence is a sequence where the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.

For example, [1, 7, 4, 9, 2, 5] is a wiggle sequence because the differences (6, -3, 5, -7, 3) are alternately positive and negative.
In contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.
A subsequence is obtained by deleting some elements (eventually, also zero) from the original sequence, leaving the remaining elements in their original order.

 

Example 1:

Input: nums = [1,7,4,9,2,5]
Output: 6
Explanation: The entire sequence is a wiggle sequence.

https://leetcode.com/problems/wiggle-subsequence/
'''
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        if len(set(nums)) < 2:
            return len(set(nums))
        inc = nums[0] < nums[1]
        i, retVal = 1, 2
        if nums[0] == nums[1]:
            retVal -= 1
            inc = "same"
        while i < len(nums)-1:
            #print(retVal, nums[i], nums[i+1], inc)
            if inc == "same":
                if nums[i] != nums[i+1]:
                    retVal += 1
                    inc = nums[i] < nums[i+1]
                i +=1 
                continue
            if inc:
                if nums[i] > nums[i+1]:
                    retVal += 1
                    inc = not inc
            if not inc:
                if nums[i] < nums[i+1]:
                    retVal += 1
                    inc = not inc
            i += 1
        return retVal
