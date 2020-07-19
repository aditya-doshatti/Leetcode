'''
210. Course Schedule II
Medium

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: 2, [[1,0]] 
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
             course 0. So the correct course order is [0,1] .

https://leetcode.com/problems/course-schedule-ii/
'''
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(set)
        neigh = collections.defaultdict(set)
        for val in prerequisites:
            graph[val[0]].add(val[1])
            neigh[val[1]].add(val[0])
        stack = [i for i in range(numCourses) if not graph[i]]
        retVal = []
        while stack:
            curr = stack.pop()
            retVal.append(curr)
            for i in neigh[curr]:
                graph[i].remove(curr)
                if not graph[i]:
                    stack.append(i)
            graph.pop(curr)
        return retVal if not graph else []
