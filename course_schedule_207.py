'''
207. Course Schedule
Medium

There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?


Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.

https://leetcode.com/problems/course-schedule/
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = defaultdict(set)
        post = defaultdict(set)
        for c1, c2 in prerequisites:
            pre[c1].add(c2)
            post[c2].add(c1)
        q = deque([course for course in range(numCourses) if course not in pre])
        courses_done = 0
        while q:
            curr = q.popleft()
            print(curr)
            courses_done += 1
            for course in post[curr]:
                pre[course].remove(curr)
                if not pre[course]:
                    q.append(course)
        return courses_done == numCourses
        # Missing few test cases
        # graph = defaultdict(list)
        # for c1, c2 in prerequisites:
        #     graph[c1].append(c2)
        # for i in range(numCourses):
        #     visited = set()
        #     q = [i] 
        #     while q:
        #         curr = q.pop(0)
        #         if curr in visited:
        #             return False
        #         q += graph[curr]
        #         visited.add(curr)
        # return True
