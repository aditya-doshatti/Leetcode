'''
1636. Sort Array by Increasing Frequency

Easy

Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

Return the sorted array.

 

Example 1:

Input: nums = [1,1,2,2,2,3]
Output: [3,1,1,2,2,2]
Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.

https://leetcode.com/problems/sort-array-by-increasing-frequency/description
'''
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        num_frequency = Counter(nums)
        retVal = sorted(nums, key=lambda x: (num_frequency[x], -x))
        return retVal
