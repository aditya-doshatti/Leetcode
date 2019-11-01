'''
665. Non-decreasing Array
Easy

Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:
Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

https://leetcode.com/problems/non-decreasing-array/
'''
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        i, cnt,temp,flag = 1, 0, nums[0], False
        while i < len(nums):
            if temp > nums[i]:
                if flag:
                    return False
                if i-2<0 or nums[i-2]<nums[i]:
                    temp = nums[i]
                flag = True
            else:
                temp = nums[i]
            i += 1
        return True
	'''
	Wrong Answer
	i, cnt = 0, 0
        while i < len(nums)-1:
            if nums[i] > nums[i+1]:
                cnt +=1
                if cnt > 1:
                    return False
            i += 1
        return True
	'''
