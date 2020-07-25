'''
797. All Paths From Source to Target
Medium

Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, and return them in any order.

The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for which the edge (i, j) exists.

Example:
Input: [[1,2], [3], [3], []] 
Output: [[0,1,3],[0,2,3]] 
Explanation: The graph looks like this:
0--->1
|    |
v    v
2--->3
There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
Note:

The number of nodes in the graph will be in the range [2, 15].
You can print different paths in any order, but you should keep the order of nodes inside one path.

https://leetcode.com/problems/all-paths-from-source-to-target/
'''
class Solution:
    def __init__(self):
        self.retVal = []
        
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        curr = [0]
        visited = [False] * len(graph)
        self.helper(graph, curr)
        return self.retVal
    
    def helper(self, graph, curr):
        for node in graph[curr[-1]]:
            if node == len(graph) -1 :
                curr.append(node)
                copy = curr[::]
                self.retVal.append(copy)
                curr.pop(-1)
            else:
                curr.append(node)
                self.helper(graph, curr)
        curr.pop(-1)
