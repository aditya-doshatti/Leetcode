'''
478. Generate Random Point in a Circle
Medium

Given the radius and x-y positions of the center of a circle, write a function randPoint which generates a uniform random point in the circle.

Note:

input and output values are in floating-point.
radius and x-y position of the center of the circle is passed into the class constructor.
a point on the circumference of the circle is considered to be in the circle.
randPoint returns a size 2 array containing x-position and y-position of the random point, in that order.
Example 1:

Input: 
["Solution","randPoint","randPoint","randPoint"]
[[1,0,0],[],[],[]]
Output: [null,[-0.72939,-0.65505],[-0.78502,-0.28626],[-0.83119,-0.19803]]

https://leetcode.com/problems/generate-random-point-in-a-circle/
'''
import random
class Solution(object):

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.r, self.x, self.y = radius, x_center, y_center

    def randPoint(self):
        """
        :rtype: List[float]
        """
        while True:
            ranx = round(random.uniform(self.x-self.r, self.x+self.r), 5)
            rany = round(random.uniform(self.y-self.r, self.y+self.r), 5)
            eq = (ranx - self.x)**2 + (rany - self.y)**2
            if eq < self.r**2:
                return [ranx, rany]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
