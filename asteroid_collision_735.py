'''
735. Asteroid Collision
Medium

We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.

https://leetcode.com/problems/asteroid-collision/
'''
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        retVal = []
        for val in asteroids:
            if val > 0:
                retVal.append(val)
            else:
                while retVal and retVal[-1] > 0 and retVal[-1] < abs(val):
                    retVal.pop()
                if not retVal or retVal[-1]<0:
                    retVal.append(val)
                elif retVal[-1] == abs(val):
                    retVal.pop()
        return retVal
