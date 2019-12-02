'''
740. Delete and Earn
Medium

Given an array nums of integers, you can perform operations on the array.

In each operation, you pick any nums[i] and delete it to earn nums[i] points. After, you must delete every element equal to nums[i] - 1 or nums[i] + 1.

You start with 0 points. Return the maximum number of points you can earn by applying such operations.

Example 1:

Input: nums = [3, 4, 2]
Output: 6
Explanation: 
Delete 4 to earn 4 points, consequently 3 is also deleted.
Then, delete 2 to earn 2 points. 6 total points are earned.

https://leetcode.com/problems/delete-and-earn/
'''
class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = {}
        for n in nums:
            c[n] = c.get(n, 0) + 1
        prev = None
        val1, val2 = 0, 0
        for key in sorted(c):
            if key-1 != prev:
                val1, val2 = max(val1, val2), key*c[key] + max(val1, val2)
            else:
                val1, val2 = max(val1, val2), key*c[key] + val1
            prev = key
        return max(val1, val2)
