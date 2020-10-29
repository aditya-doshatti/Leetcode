'''
228. Summary Ranges
Easy

You are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
 

Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

https://leetcode.com/problems/summary-ranges/
'''
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        i, j = 0, 1
        counter = 1
        retVal = []
        while j < len(nums):
            if nums[j] - counter == nums[i]:
                counter += 1
                j += 1
                continue
            else:
                if counter == 1:
                    retVal.append(str(nums[i]))
                    i += 1
                    j = i + 1
                else:
                    retVal.append(str(nums[j-1]-counter+1) + '->' + str(nums[j-1]))
                    counter = 1
                    i = j 
                    j = i + 1
        if not retVal or ((str(nums[-1]) in retVal[-1]) and ('->' in retVal[-1])) or str(nums[-1]) not in retVal[-1]:
            if counter == 1:
                retVal.append(str(nums[-1]))
            else:
                retVal.append(str(nums[j-1]-counter+1) + '->' + str(nums[j-1]))
        return retVal
