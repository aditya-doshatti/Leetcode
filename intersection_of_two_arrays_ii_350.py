'''
350. Intersection of Two Arrays II
Easy

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

https://leetcode.com/problems/intersection-of-two-arrays-ii/
'''
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            counter = Counter(nums2)
            it = nums1
        else:
            counter = Counter(nums1)
            it = nums2
        retVal = []
        for val in it:
            if val in counter and counter[val] > 0:
                retVal.append(val)
                counter[val] -= 1
        return retVal
