'''
733. Flood Fill
Easy

An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input: 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.

https://leetcode.com/problems/flood-fill/
'''
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image or len(image) == 0 : return 0
        val = image[sr][sc]
        if val == newColor:
            return image
        q = set({(sr,sc)})
        while q:
            curi, curj = q.pop()
            image[curi][curj] = newColor
            for i,j in ((-1,0), (0,-1), (0,1), (1,0)):
                tempi ,tempj = curi + i, curj + j
                if tempi >= 0 and tempi < len(image) and tempj >= 0 and tempj < len(image[tempi]):
                        if image[tempi][tempj] == val:
                            q.add((tempi, tempj))
        return image
