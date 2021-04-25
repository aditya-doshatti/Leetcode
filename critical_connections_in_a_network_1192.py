'''
1192. Critical Connections in a Network
Hard

There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server unable to reach some other server.

Return all critical connections in the network in any order.

 

Example 1:



Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.

https://leetcode.com/problems/critical-connections-in-a-network/
'''
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = [[] for i in range(n)]
        depth = [-1] * n
        retVal = []
        for p, q in connections:
            graph[p].append(q)
            graph[q].append(p)
        def dfs(prev, cur, dep): # from, to, depth
            dep2 = depth[cur] = dep
            for nbr in graph[cur]:
                if nbr == prev: 
                    continue
                dep3 = depth[nbr] if depth[nbr] >= 0 else dfs(cur, nbr, dep+1)
                if dep3 > dep: 
                    retVal.append((cur, nbr))
                elif dep2 > dep3: 
                    dep2 = dep3
            depth[cur] = dep2
            return dep2
        dfs(0,0,0)
        return retVal
