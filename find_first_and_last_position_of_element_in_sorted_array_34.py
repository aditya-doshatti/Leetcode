'''
34. Find First and Last Position of Element in Sorted Array
Medium

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums)<1:
            return [-1,-1]
        l, r, first, last = 0, len(nums)-1, -1, -1
        while l < r:
            mid = (l+r)//2
            if nums[mid]<target:
                l = mid+1
            else:
                r = mid
        if nums[l] != target:
            return [-1,-1]
        first = l
        l, r = first, len(nums)-1
        while l < r:
            mid = (l+r)//2
            if nums[mid+1] == target:
                l = mid + 1
            else:
                r = mid
        last = l
        return [first, last]  
'''
Earlier submission

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1,-1]
        return self.helper(nums, 0, len(nums)-1, target)
    
    def helper(self, nums, s, e, target):
        #print s, e
        if (s==e and nums[s] != target):
            return [-1,-1]
        if (abs(s-e) == 1):
            if nums[s] != target and nums[e] != target:
                return [-1,-1]
            elif nums[s] == target and nums[e] == target:
                return [s,e]
            elif nums[s] == target:
                return [s,s]
            else:
                return [e,e]            
        mid = (s+e)/2
        if(nums[mid] == target):
            first, last = mid, mid
            while first >= s:
                if nums[first - 1] == target and first > 0:
                    first = first - 1
                else:
                    break
            while last < e:
                if nums[last + 1] == target:
                    last += 1
                else:
                    break
            #print last, first
            return [first, last]
        else:
            if nums[mid] > target:
                return self.helper(nums, s, mid, target)
            else:
                return self.helper(nums, mid, e, target)
'''     
