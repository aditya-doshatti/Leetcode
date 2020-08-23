'''
497. Random Point in Non-overlapping Rectangles
Medium

Given a list of non-overlapping axis-aligned rectangles rects, write a function pick which randomly and uniformily picks an integer point in the space covered by the rectangles.

Note:

An integer point is a point that has integer coordinates. 
A point on the perimeter of a rectangle is included in the space covered by the rectangles. 
ith rectangle = rects[i] = [x1,y1,x2,y2], where [x1, y1] are the integer coordinates of the bottom-left corner, and [x2, y2] are the integer coordinates of the top-right corner.
length and width of each rectangle does not exceed 2000.
1 <= rects.length <= 100
pick return a point as an array of integer coordinates [p_x, p_y]
pick is called at most 10000 times.
Example 1:

Input: 
["Solution","pick","pick","pick"]
[[[[1,1,5,5]]],[],[],[]]
Output: 
[null,[4,1],[4,1],[3,3]]

https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/
'''
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        weight, c = [], 0
        for rect in rects:
            x1, y1, x2, y2 = rect
            c += (x2-x1+1)*(y2-y1+1)
            weight.append(c)
        self.weightc = [w/c for w in weight]

    def pick(self) -> List[int]:
        u = random.random()
        ix = bisect.bisect_left(self.weightc, u)
        x1, y1, x2, y2 = self.rects[ix]
        x = random.randint(x1,x2)
        y = random.randint(y1,y2)
        return [x,y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
