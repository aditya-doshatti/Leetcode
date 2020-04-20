'''
33. Search in Rotated Sorted Array
Medium

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

https://leetcode.com/problems/search-in-rotated-sorted-array/
'''
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.searchBin(nums, 0, len(nums)-1, target)
        
    def searchBin (self, arr, l, h, key): 
        if l > h: 
            return -1

        mid = (l + h) // 2
        if arr[mid] == key: 
            return mid 

        # If arr[l...mid] is sorted  
        if arr[l] <= arr[mid]: 

            # As this subarray is sorted, we can quickly 
            # check if key lies in half or other half  
            if key >= arr[l] and key <= arr[mid]: 
                return self.searchBin(arr, l, mid-1, key) 
            return self.searchBin(arr, mid+1, h, key) 

        # If arr[l..mid] is not sorted, then arr[mid... r] 
        # must be sorted 
        if key >= arr[mid] and key <= arr[h]: 
            return self.searchBin(arr, mid+1, h, key) 
        return self.searchBin(arr, l, mid-1, key)
