'''
227. Basic Calculator II
Medium

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7

https://leetcode.com/problems/basic-calculator-ii/
'''
class Solution:
    def calculate(self, s: str) -> int:
        s += '$'
        stack = [0]
        last = '+'
        for c in s:
            if c.isdigit():
                stack[-1] = stack[-1]*10 + int(c)
            elif c in "+-*/$":
                if last == '-':
                    stack[-1] *= -1
                elif last == '*':
                    x = stack.pop()
                    stack[-1] *= x
                elif last == '/':
                    x = stack.pop()
                    stack[-1] = int(stack[-1]/x)
                stack.append(0)
                last = c
        return sum(stack)
        # nums, operations, syms = [], [], {'+', '-', '*', '/'}
        # for char in s:
        #     if '0' <= char <= '9':
        #         if not nums:
        #             nums.append('')
        #         nums[-1] += char
        #     elif char in syms:
        #         nums.append('')
        #         operations.append(char)
        # while '/' in operations:
        #     k = operations.index('/')
        #     operations.pop(k)
        #     nums[k] = str(int(nums[k])//int(nums[k+1]))
        #     del nums[k+1]
        # while '*' in operations:
        #     k = operations.index('*')
        #     operations.pop(k)
        #     nums[k] = str(int(nums[k])*int(nums[k+1]))
        #     del nums[k+1]
        # k = 0
        # while operations:
        #     op = operations.pop(0)
        #     if op == '+':
        #         nums[k] = str(int(nums[k])+int(nums[k+1]))
        #     elif op == "-":
        #         nums[k] = str(int(nums[k])-int(nums[k+1]))
        #     del nums[k+1]
        # return int(nums[0])
