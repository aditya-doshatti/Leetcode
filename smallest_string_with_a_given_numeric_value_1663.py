'''
1663. Smallest String With A Given Numeric Value
Medium

The numeric value of a lowercase character is defined as its position (1-indexed) in the alphabet, so the numeric value of a is 1, the numeric value of b is 2, the numeric value of c is 3, and so on.

The numeric value of a string consisting of lowercase characters is defined as the sum of its characters' numeric values. For example, the numeric value of the string "abe" is equal to 1 + 2 + 5 = 8.

You are given two integers n and k. Return the lexicographically smallest string with length equal to n and numeric value equal to k.

Note that a string x is lexicographically smaller than string y if x comes before y in dictionary order, that is, either x is a prefix of y, or if i is the first position such that x[i] != y[i], then x[i] comes before y[i] in alphabetic order.

 

Example 1:

Input: n = 3, k = 27
Output: "aay"
Explanation: The numeric value of the string is 1 + 1 + 25 = 27, and it is the smallest string with such a value and length equal to 3.

https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/
'''
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        if n*26 == k:
            return 'z'*n
        k -= n
        NoZ = k//25
        NoA = n-NoZ-1
        return 'a'*NoA + chr(ord('a')+k%25) + 'z'*NoZ
        # NOT BEST TIME
        # string = '0abcdefghijklmnopqrstuvwxyz'
        # retVal = ''
        # while n > 0:
        #     curr = min(26, k - n + 1)
        #     retVal = string[curr] + retVal
        #     k -= curr
        #     n -= 1
        # return retVal
        # TLE
        # string = '0abcdefghijklmnopqrstuvwxyz'
        # retVal = ''
        # while k > 0:
        #     curr = min(26, k)
        #     while curr > 0:
        #         if k - curr >= n-1:
        #             retVal = string[curr] + retVal
        #             k -= curr
        #             n -= 1
        #             break
        #         else:
        #             curr -= 1
        # return retVal
