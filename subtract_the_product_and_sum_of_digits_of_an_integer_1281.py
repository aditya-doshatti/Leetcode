'''
1281. Subtract the Product and Sum of Digits of an Integer
Easy

Given an integer number n, return the difference between the product of its digits and the sum of its digits.
 

Example 1:

Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15

https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
'''
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sumVal, productVal = 0, 1
        while n > 0:
            digit = n % 10
            sumVal += digit
            productVal *= digit
            n//=10
        return productVal - sumVal
