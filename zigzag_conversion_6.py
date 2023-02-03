'''
6. Zigzag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
'''
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if s is None and numRows <= 0:
            return ''
        if numRows == 1:
            return s
        retVal = ''
        jump = 2 * numRows - 2
        for i in range(0, numRows):
            for j in range(i, len(s), jump):
                retVal += s[j]
                if i != 0 and i != numRows - 1 and (j + jump - 2 * i) < len(s):
                    retVal += s[j + jump - 2 * i]
        return retVal
