'''
456. 132 Pattern
Medium

Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such that i < j < k and ai < ak < aj. Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.

Note: n will be less than 15,000.

Example 1:
Input: [1, 2, 3, 4]

Output: False

Explanation: There is no 132 pattern in the sequence.

https://leetcode.com/problems/132-pattern/
'''
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        minVal = float('-inf')
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < minVal:
                return True
            while stack and stack[-1] < nums[i]:
                minVal = stack.pop()
            stack.append(nums[i])
        return False
        # TLE
        # if not nums or len(nums) < 3:
        #     return False
        # minVal = nums[0]
        # for i in range(1, len(nums)):
        #     if nums[i] > minVal:
        #         for j in range(i+1, len(nums)):
        #             if nums[j] < nums[i] and nums[j] > minVal:
        #                 return True
        #     minVal = min(minVal, nums[i])
        # return False
        # Failed attempt
        # flag = 2
        # prev = maxVal = nums[0]
        # for i in range(1,len(nums)):
        #     print("before", flag, nums[i], prev, maxVal)
        #     if flag == 2:
        #         if nums[i] > prev:
        #             maxVal = nums[i]
        #             flag -= 1
        #         else:
        #             prev = min(prev, nums[i])
        #     elif flag == 1:
        #         if nums[i] > prev and nums[i] < maxVal:
        #             flag -=1
        #             return True
        #         elif nums[i] < prev:
        #             prev = maxVal
        #             maxVal = nums[i]
        #     print("after", flag, nums[i], prev, maxVal)
        # return False
