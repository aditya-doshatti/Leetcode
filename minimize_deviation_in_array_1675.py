'''
1675. Minimize Deviation in Array
Hard

You are given an array nums of n positive integers.

You can perform two types of operations on any element of the array any number of times:

If the element is even, divide it by 2.
For example, if the array is [1,2,3,4], then you can do this operation on the last element, and the array will be [1,2,3,2].
If the element is odd, multiply it by 2.
For example, if the array is [1,2,3,4], then you can do this operation on the first element, and the array will be [2,2,3,4].
The deviation of the array is the maximum difference between any two elements in the array.

Return the minimum deviation the array can have after performing some number of operations.

Example 1:

Input: nums = [1,2,3,4]
Output: 1
Explanation: You can transform the array to [1,2,3,2], then to [2,2,3,2], then the deviation will be 3 - 2 = 1.

https://leetcode.com/problems/minimize-deviation-in-array/
'''
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heap, maxVal = [], float("-inf")
        for num in nums:
            tmp = num
            while tmp%2 == 0:
                tmp//=2
            heap.append((tmp, max(num, tmp*2)))
            maxVal = max(maxVal, tmp)
        heapify(heap)
        retVal = float("inf")
        while len(heap) == len(nums):
            val, lim  = heappop(heap)
            retVal = min(retVal, maxVal - val)
            if val < lim:
                heappush(heap, (val*2, lim))
                maxVal = max(maxVal, val*2)
        return retVal
