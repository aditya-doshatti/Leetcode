'''
34. Increasing Triplet Subsequence
Medium

Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

Example 1:

Input: [1,2,3,4,5]
Output: true

https://leetcode.com/problems/increasing-triplet-subsequence/
'''
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallest, bigger,i= float('inf'), float('inf'),0
        while i < len(nums):
            if nums[i] < smallest:
                smallest = nums[i]
            elif nums[i] > smallest and nums[i] < bigger:
                bigger = nums[i]
            elif nums[i] > smallest and nums[i] > bigger:
                return True
            i+=1
        else:
            return False
