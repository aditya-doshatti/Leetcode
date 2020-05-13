'''
540. Single Element in a Sorted Array
Medium

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

 

Example 1:

Input: [1,1,2,3,3,4,4,8,8]
Output: 2

https://leetcode.com/problems/single-element-in-a-sorted-array/
'''
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        i, j = 0, len(nums)-1
        while i < j:
            mid = (i+j) // 2
            if nums[mid] == nums[mid-1]:
                if (mid-i) % 2 == 0:
                    j = mid - 2
                else:
                    i = mid + 1
            else:
                if (mid-i) % 2:
                    j = mid -1
                else:
                    i = mid
        return nums[i]
