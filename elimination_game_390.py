'''
390. Elimination Game
Medium

There is a list of sorted integers from 1 to n. Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.

Repeat the previous step again, but this time from right to left, remove the right most number and every other number from the remaining numbers.

We keep repeating the steps again, alternating left to right and right to left, until a single number remains.

Find the last number that remains starting with a list of length n.

Example:

Input:
n = 9,
1 2 3 4 5 6 7 8 9
2 4 6 8
2 6
6

Output:
6

https://leetcode.com/problems/elimination-game/
'''
class Solution:
    def lastRemaining(self, n: int) -> int:
        return self.helper(n, 1)

    def helper(self, n , flag):
        if n==1:
            return 1
        if flag:
            return 2*self.helper(n//2, 0)
        elif (n%2):
            return 2*self.helper(n//2, 1)
        else:
            return 2*self.helper(n//2, 1)-1
        # Brute Force
        # arr = range(1, n+1)
        # while len(arr) > 1:
        #     arr = arr[1::2][::-1]
        # return arr[0]
