'''
1697. Checking Existence of Edge Length Limited Paths
Solved
Hard
Topics
Companies
Hint
An undirected graph of n nodes is defined by edgeList, where edgeList[i] = [ui, vi, disi] denotes an edge between nodes ui and vi with distance disi. Note that there may be multiple edges between two nodes.

Given an array queries, where queries[j] = [pj, qj, limitj], your task is to determine for each queries[j] whether there is a path between pj and qj such that each edge on the path has a distance strictly less than limitj .

Return a boolean array answer, where answer.length == queries.length and the jth value of answer is true if there is a path for queries[j] is true, and false otherwise.

 

Example 1:


Input: n = 3, edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], queries = [[0,1,2],[0,2,5]]
Output: [false,true]
Explanation: The above figure shows the given graph. Note that there are two overlapping edges between 0 and 1 with distances 2 and 16.
For the first query, between 0 and 1 there is no path where each distance is less than 2, thus we return false for this query.
For the second query, there is a path (0 -> 1 -> 2) of two edges with distances less than 5, thus we return true for this query.

https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/description/

https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/solutions/3464929/image-explanation-easiest-complete-intuition-c-java-python
'''
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xset, yset = self.find(x), self.find(y)
        if xset != yset:
            if self.rank[xset] < self.rank[yset]:
                self.parent[xset] = yset
            else:
                self.parent[yset] = xset
            if self.rank[xset] == self.rank[yset]:
                self.rank[xset] += 1
            return True
        return False

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        dsu = DSU(n)
        for i, q in enumerate(queries):
            queries[i].append(i)

        queries.sort(key=lambda q: q[2])
        edgeList.sort(key=lambda e: e[2])

        i = 0
        res = [False] * len(queries)
        for q in queries:
            while i < len(edgeList) and edgeList[i][2] < q[2]:
                dsu.union(edgeList[i][0], edgeList[i][1])
                i += 1

            if dsu.find(q[0]) == dsu.find(q[1]):
                res[q[3]] = True

        return res
'''
TLE 14/24
class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        for edge in edgeList:
            u, v, dist = edge[0], edge[1], edge[2]
            graph[u].append((v, dist))
            graph[v].append((u, dist))
        retVal = []
        # print(graph)
        for query in queries:
            visited, found = set(), False
            q = [query[0]]
            while q:
                # print(q, visited)
                curr = q.pop(0)
                visited.add(curr)
                if curr == query[1]:
                    found = True
                    break
                for vals in graph[curr]:
                    if vals[0] not in visited:
                        if vals[1] < query[2]:
                            q.append(vals[0])
            if found:
                retVal.append(True)
            else:
                retVal.append(False)
        return retVal
'''
