'''
650. 2 Keys Keyboard
Medium

Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each step:

Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
Paste: You can paste the characters which are copied last time.
 

Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted. Output the minimum number of steps to get n 'A'.

Example 1:

Input: 3
Output: 3
Explanation:
Intitally, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.

https://leetcode.com/problems/2-keys-keyboard/
'''
class Solution:
    def minSteps(self, n: int) -> int:
        retVal = 0
        factor = 2
        while n > 1:
            while n % factor == 0:
                retVal += factor
                n /= factor
            factor +=1
        return retVal
