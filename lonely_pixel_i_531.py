'''
531. Lonely Pixel I
Medium

Given an m x n picture consisting of black 'B' and white 'W' pixels, return the number of black lonely pixels.

A black lonely pixel is a character 'B' that located at a specific position where the same row and same column don't have any other black pixels.

 

Example 1:


Input: picture = [["W","W","B"],["W","B","W"],["B","W","W"]]
Output: 3
Explanation: All the three 'B's are black lonely pixels.

https://leetcode.com/problems/lonely-pixel-i/
'''
class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        row, col, setVal, retVal = defaultdict(int), defaultdict(int), set(),0
        for i in range(len(picture)):
            for j in range(len(picture[0])):
                if picture[i][j] == 'B':
                    row[i] += 1
                    col[j] += 1
                    setVal.add((i,j))
        for x,y in setVal:
            if row[x] ==1 and col[y] == 1:
                retVal += 1
        return retVal
