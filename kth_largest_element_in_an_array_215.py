'''
215. Kth Largest Element in an Array
Medium

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5

https://leetcode.com/problems/kth-largest-element-in-an-array/
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums: 
            return
        pivot = random.choice(nums)
        smaller, equal, greater = [], [], []
        for x in nums:
            if x > pivot:
                smaller.append(x)
            if x == pivot:
                equal.append(x)
            if x < pivot:
                greater.append(x)        
        if k <= len(smaller):
            return self.findKthLargest(smaller, k)
        elif k > len(smaller) + len(equal):
            return self.findKthLargest(greater, k - len(smaller) - len(equal))
        else:
            return equal[0]
