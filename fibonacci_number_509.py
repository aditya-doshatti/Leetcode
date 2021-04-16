'''
509. Fibonacci Number
Easy

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

 

Example 1:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

https://leetcode.com/problems/fibonacci-number/
'''
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        self.dic = {0:0, 1:1}
        return self.fillDic(n)

    def fillDic(self, n):
        if n in self.dic:
            return self.dic[n]
        self.dic[n] =self.fillDic(n-1) + self.fillDic(n-2)
        return self.fillDic(n)
