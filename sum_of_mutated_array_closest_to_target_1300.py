'''
1300. Sum of Mutated Array Closest to Target
Medium

Given an integer array arr and a target value target, return the integer value such that when we change all the integers larger than value in the given array to be equal to value, the sum of the array gets as close as possible (in absolute difference) to target.

In case of a tie, return the minimum such integer.

Notice that the answer is not neccesarilly a number from arr.

 

Example 1:

Input: arr = [4,9,3], target = 10
Output: 3
Explanation: When using 3 arr converts to [3, 3, 3] which sums 9 and that's the optimal answer.

https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/
'''
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        mx, sumVal = 1, 0
        for val in arr:
            mx = max(mx, val)
            sumVal += val
        if len(arr) == 1:
            return arr[0]
        if sumVal < target:
            return mx
        left, right, retVal, curr = 0, mx, 0, float('inf')
        while left <= right:
            mid = (left + right) // 2
            currSum = 0
            for i in arr:
                if i <= mid:
                    currSum += i
                else:
                    currSum += mid
            if currSum == target:
                return mid
            diff = abs(target - currSum)
            if diff < curr:
                curr = diff
                retVal = mid
            elif diff == curr:
                retVal = min(retVal, mid)
            if currSum > target:
                right = mid - 1
            else:
                left = mid + 1
        return retVal
