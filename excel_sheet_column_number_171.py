'''
171. Excel Sheet Column Number
Easy

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1

https://leetcode.com/problems/excel-sheet-column-number/
'''
class Solution:
    def titleToNumber(self, s: str) -> int:
        retVal = 0
        for char in s:
            retVal *= 26
            retVal += ord(char) - ord('A') + 1
        return retVal
