'''
754. Reach a Number
Medium

You are standing at position 0 on an infinite number line. There is a goal at position target.

On each move, you can either go left or right. During the n-th move (starting from 1), you take n steps.

Return the minimum number of steps required to reach the destination.

Example 1:
Input: target = 3
Output: 2
Explanation:
On the first move we step from 0 to 1.
On the second step we step from 1 to 3.

https://leetcode.com/problems/reach-a-number/
'''
class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        i = 0
        while target > 0:
            i += 1
            target -= i
        return i if target % 2 == 0 else i + 1 + i%2
