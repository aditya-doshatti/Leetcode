'''
277. Find the Celebrity

Medium

Suppose you are at a party with n people labeled from 0 to n - 1 and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know the celebrity, but the celebrity does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. You are only allowed to ask questions like: "Hi, A. Do you know B?" to get information about whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) that tells you whether a knows b. Implement a function int findCelebrity(n). There will be exactly one celebrity if they are at the party.

Return the celebrity's label if there is a celebrity at the party. If there is no celebrity, return -1.

 

Example 1:


Input: graph = [[1,1,0],[0,1,0],[1,1,1]]
Output: 1
Explanation: There are three persons labeled with 0, 1 and 2. graph[i][j] = 1 means person i knows person j, otherwise graph[i][j] = 0 means person i does not know person j. The celebrity is the person labeled as 1 because both 0 and 2 know him but 1 does not know anybody.

https://leetcode.com/problems/find-the-celebrity/description/
'''
# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        celeb, i = 0, 1
        while i < n:
            if knows(celeb, i) or not knows(i, celeb):
                celeb = i
            i += 1
        for i in range(n):
            if i != celeb:
                if knows(celeb, i) or not knows(i, celeb):
                    return -1
        return celeb
        '''
        TLE 152/180
        if n == 2:
            if knows(0,1) and not knows(1,0):
                return 1
            elif knows(1,0) and not knows(0,1):
                return 0
            return -1
        not_celeb, celeb = set(), set()
        for i in range(n):
            for j in range(n):
                if i != j:
                    if knows(i, j):
                        if not knows(j,i) and j not in not_celeb:
                            celeb.add(j)
                        not_celeb.add(i)
                        if i in celeb:
                            celeb.remove(i)
        if len(celeb) == 1:
            val = celeb.pop()
            for j in range(n):
                if j!=val:
                    if not knows(j,val):
                        return -1
            return val
        return -1
        '''
