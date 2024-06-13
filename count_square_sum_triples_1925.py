'''
1925. Count Square Sum Triples

Easy

A square triple (a,b,c) is a triple where a, b, and c are integers and a2 + b2 = c2.

Given an integer n, return the number of square triples such that 1 <= a, b, c <= n.

 

Example 1:

Input: n = 5
Output: 2
Explanation: The square triples are (3,4,5) and (4,3,5).

https://leetcode.com/problems/count-square-sum-triples/description/
'''
class Solution:
    def countTriples(self, n: int) -> int:
        retVal, maxVal = 0, n*n
        for i in range(1, n):
            for j in range(i+1, n):
                currSq = i*i + j*j
                if currSq > maxVal:
                    break
                if sqrt(currSq) % 1 == 0:
                    retVal += 2
        return retVal
        '''
        Wrong answer 10/91
        squares, sums, retVal = {1}, set(), 0
        for i in range(2,n + 1):
            print(sums)
            currSq = i ** 2
            if currSq in sums:
                print(currSq)
                retVal += 2
            for val in squares:
                sums.add(currSq + val)
            squares.add(currSq)
        return retVal
        '''
