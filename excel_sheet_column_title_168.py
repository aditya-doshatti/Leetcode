'''
168. Excel Sheet Column Title
Easy

Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

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

Input: columnNumber = 1
Output: "A"

https://leetcode.com/problems/excel-sheet-column-title/
'''
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while(columnNumber>0):
            endNumber = (columnNumber-1)%26
            columnNumber = (columnNumber-1)//26
            result = chr(endNumber+65) + result
        return result
