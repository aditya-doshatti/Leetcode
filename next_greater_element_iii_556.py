'''
556. Next Greater Element III
Medium

Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.

 

Example 1:

Input: n = 12
Output: 21

https://leetcode.com/problems/next-greater-element-iii/
'''
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        idx = len(digits) - 1
        while idx - 1 >= 0 and digits[idx] <= digits[idx - 1]:
            idx -= 1			
        if idx == 0:
            return -1		
        bigger = idx		
        while bigger + 1 < len(digits) and digits[bigger + 1] > digits [idx - 1]:
            bigger += 1		
        digits[bigger], digits[idx - 1] = digits[idx - 1], digits[bigger]
        digits[idx :] = digits[idx :][::-1]		
        digits = int("".join(digits))		
        return digits if digits < 1 << 31 else -1
        # string = list(str(n))
        # string.sort()
        # print(string)
        # i = 0
        # while i < len(string):
        #     print(''.join(string[i:])+ ''.join(string[:i]))
        #     if int(''.join(string[i:]) + ''.join(string[:i])) > n:
        #         pass
        #         #return int(string[i:] + string[:i])
        #     i+=1
        # return -1
