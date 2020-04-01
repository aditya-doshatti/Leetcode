'''
834. Sum of Distances in Tree
Hard

An undirected, connected tree with N nodes labelled 0...N-1 and N-1 edges are given.

The ith edge connects nodes edges[i][0] and edges[i][1] together.

Return a list ans, where ans[i] is the sum of the distances between node i and all other nodes.

Example 1:

Input: N = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
Output: [8,12,6,10,10,10]
Explanation: 
Here is a diagram of the given tree:
  0
 / \
1   2
   /|\
  3 4 5
We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
equals 1 + 1 + 2 + 2 + 2 = 8.  Hence, answer[0] = 8, and so on.

https://leetcode.com/problems/sum-of-distances-in-tree/
'''
class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        dic = defaultdict(list)
        for edge in edges:
            dic[edge[0]].append(edge[1])
            dic[edge[1]].append(edge[0])
        size, parents, children = [1] * N, [0] * N, [0] * N
        
        def post(parent, idx):
            for child in dic[idx]:
                if child != parent:
                    post(idx, child)
                    size[idx] += size[child]
                    parents[idx] += parents[child] + size[child]
                
        def pre(parent, idx):
            if parent != -1:
                children[idx] = children[parent] + (parents[parent] - parents[idx] - size[idx]) + (N-size[idx])
            for child in dic[idx]:
                if child != parent:
                    pre(idx, child)
        post(-1, 0)
        pre(-1, 0)
        return [parents[i] + children[i] for i in range(N)]
        # My solution passes 65/69 test cases rest time out (N = 10,000)
        # dic = defaultdict(list)
        # for edge in edges:
        #     dic[edge[0]].append(edge[1])
        #     dic[edge[1]].append(edge[0])
        # # print(dic)
        # retVal = [float('-inf') for _ in range(N)]
        # for i in range(N):
        #     temp = [float('-inf') for _ in range(N)]
        #     temp[i] = 0
        #     for val in dic[i]:
        #         temp[val] = 1
        #     pending = []
        #     for j in range(len(temp)):
        #         if temp[j] != float('-inf'):
        #             continue
        #         else:
        #             for val in dic[j]:
        #                 if temp[val]>0:
        #                     temp[j] = temp[val]+1
        #                     break
        #             if temp[j] == float('-inf'):
        #                 pending.append(j)
        #     # print(temp)
        #     while pending:
        #         # print(pending)
        #         j = pending.pop(0)
        #         if temp[j] != float('-inf'):
        #             continue
        #         else:
        #             for val in dic[j]:
        #                 # print(temp[val], val, j)
        #                 if temp[val]>0:
        #                     temp[j] = temp[val]+1
        #                     break
        #             if temp[j] == float('-inf'):
        #                 pending.append(j)
        #     # print(i, temp)
        #     retVal[i] = sum(temp)
        # return retVal
                    
        
