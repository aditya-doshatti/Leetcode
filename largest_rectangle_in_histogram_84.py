'''
84. Largest Rectangle in Histogram
Hard

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

 


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

 


The largest rectangle is shown in the shaded area, which has area = 10 unit.

 

Example:

Input: [2,1,5,6,2,3]
Output: 10

https://leetcode.com/problems/largest-rectangle-in-histogram/
'''
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack, retVal = [], 0
        for i, h in enumerate(heights + [0]):
            while stack and heights[stack[-1]] >= h:
                H = heights[stack.pop()]
                W = i if not stack else i-stack[-1]-1
                retVal = max(retVal, H*W)
            stack.append(i)
        return retVal
