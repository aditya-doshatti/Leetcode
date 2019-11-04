'''
912. Sort an Array
Medium

Given an array of integers nums, sort the array in ascending order.

 

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]

https://leetcode.com/problems/sort-an-array/
'''
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(0, len(nums)-1, nums)
        return nums
    #Quick sort implementation
    def quickSort(self, l, h, nums):
        if l < h:
            pivot = self.partition(l, h, nums)
            self.quickSort(l, pivot-1, nums)
            self.quickSort(pivot+1, h, nums)
    
    def partition(self, l, h, nums):
        i,j, pivot = l-1, l, nums[h]
        while j < h:
            if nums[j] < pivot:
                i += 1
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
            j += 1
        nums[h] = nums[i+1]
        nums[i+1] = pivot
        return i+1   
