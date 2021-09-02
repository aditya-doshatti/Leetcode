'''
565. Array Nesting
Medium
You are given an integer array nums of length n where nums is a permutation of the numbers in the range [0, n - 1].

You should build a set s[k] = {nums[k], nums[nums[k]], nums[nums[nums[k]]], ... } subjected to the following rule:

The first element in s[k] starts with the selection of the element nums[k] of index = k.
The next element in s[k] should be nums[nums[k]], and then nums[nums[nums[k]]], and so on.
We stop adding right before a duplicate element occurs in s[k].
Return the longest length of a set s[k].

 

Example 1:

Input: nums = [5,4,0,3,1,6,2]
Output: 4
Explanation: 
nums[0] = 5, nums[1] = 4, nums[2] = 0, nums[3] = 3, nums[4] = 1, nums[5] = 6, nums[6] = 2.
One of the longest sets s[k]:
s[0] = {nums[0], nums[5], nums[6], nums[2]} = {5, 6, 2, 0}

https://leetcode.com/problems/array-nesting/
'''
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        retVal = cnt = 0
        for i, val in enumerate(nums):
            if val == -1: 
                continue
            while nums[val] != -1:
                cnt, nums[val], val = cnt+1, -1, nums[val]
            else:    
                retVal = max(retVal, cnt)
                cnt = 0
        return retVal
        # retVal = 1
        # visited = set()
        # for i in range(len(nums)):
        #     retSet = [nums[i]]
        #     while nums[retSet[-1]] not in visited:
        #         # print(nums[retSet[-1]], visited, retSet)
        #         retSet.append(nums[retSet[-1]])
        #         visited.add(nums[retSet[-2]])
        #         # print(nums[retSet[-1]], visited, retSet)
        #         retVal = max(len(retSet)-1, retVal)
        # return retVal
