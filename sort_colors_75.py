'''
75. Sort Colors
Medium

Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

https://leetcode.com/problems/sort-colors/
'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last0, last1 = 0, 0
        for i in range(len(nums)):
            j = nums[i]
            nums[i] = 2
            if j < 2:
                nums[last1] = 1
                last1 += 1
            if j == 0:
                nums[last0] = 0
                last0+=1
