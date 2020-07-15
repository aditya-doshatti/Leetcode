'''
1344. Angle Between Hands of a Clock
Medium

Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.

 

Example 1:



Input: hour = 12, minutes = 30
Output: 165

https://leetcode.com/problems/angle-between-hands-of-a-clock/
'''
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angel_of_mins = (minutes%60) * 6
        angle_of_hours = ((hour%12) * 30) + (minutes * 0.5)
        return min(abs(angel_of_mins-angle_of_hours), abs(360-abs(angel_of_mins-angle_of_hours)))
