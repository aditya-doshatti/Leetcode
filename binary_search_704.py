'''
704. Binary Search
Easy

Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.


Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

https://leetcode.com/problems/binary-search/
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums)
        while l < h:
            mid = (l+h)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                h = mid
            else:
                l = mid + 1
        return -1
