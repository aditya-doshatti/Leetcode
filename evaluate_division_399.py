'''
399. Evaluate Division
Medium

You are given equations in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating-point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.

 

Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]

https://leetcode.com/problems/evaluate-division/
'''
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(list)
        for index, vertices in enumerate(equations):
            f, t = vertices
            graph[f].append((t, values[index]))
            graph[t].append((f, 1/values[index]))
        return [self.dfs(x, y, graph, set(), 1.0) for x, y in queries]

    def dfs(self, x, y, graph, visited, value):
        if x not in graph or y not in graph or x in visited: 
            return -1.0
        if x == y: 
            return value
        visited.add(x)
        tmp = 0
        for i in range(len(graph[x])):
            tmp = self.dfs(graph[x][i][0], y, graph, visited, graph[x][i][1]*value)
            if tmp != -1.0:
                return tmp
        return -1.0
