'''
31. Next Permutation
Medium

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]

https://leetcode.com/problems/next-permutation/
'''
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(L, start, end):
            while start < end:
                L[start], L[end] = L[end], L[start]
                start, end = start + 1, end - 1
        peak, n = len(nums) - 1, len(nums)
        while peak >= 1 and nums[peak] <= nums[peak-1]:
            peak-= 1
        print(peak, nums[peak])
        if peak != 0:
            nextSmall = peak
            while nextSmall + 1 < n and nums[nextSmall+1] > nums[peak - 1]:
                nextSmall += 1
            print(nextSmall, nums[nextSmall])
            nums[peak-1], nums[nextSmall] = nums[nextSmall], nums[peak-1]
        reverse(nums, peak, n - 1)
