'''
946. Validate Stack Sequences
Medium

Given two sequences pushed and popped with distinct values, return true if and only if this could have been the result of a sequence of push and pop operations on an initially empty stack.

 

Example 1:

Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

https://leetcode.com/problems/validate-stack-sequences/
'''
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        for val in pushed:
            if val == popped[i]:
                i += 1
                while i < len(popped) and stack and stack[-1] == popped[i]:
                    i += 1
                    stack.pop()
            else:
                stack.append(val)
        if not stack:
            return True
        return stack[::-1] == popped[i:]
