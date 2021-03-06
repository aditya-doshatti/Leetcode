'''
66. Plus One
Easy

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

https://leetcode.com/problems/plus-one/
'''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i, k = len(digits)-1, 1
        while k and i >=0 :
            digits[i] += 1
            if digits[i] == 10:
                digits[i] = 0
            else:
                k = 0
            i-=1
        if digits[0] == 0:
            digits = [1] + digits
        return digits
