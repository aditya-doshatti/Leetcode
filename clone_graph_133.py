'''
133. Clone Graph
Medium

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity sake, each node's value is the same as the node's index (1-indexed). For example, the first node with val = 1, the second node with val = 2, and so on. The graph is represented in the test case using an adjacency list.

Adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

 

Example 1:


Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

https://leetcode.com/problems/clone-graph/
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited= []
        lst = []
        adj = []
        nodeList = []
        if not node:
            return node
        for item in node.neighbors:
            adj.append(item.val)
            lst.append(item)
        head = Node(val=node.val, neighbors = adj)
        visited.append(head.val)
        curr = len(visited)
        if len(nodeList) < head.val:
            for i in range(head.val):
                nodeList.append(None)
        nodeList[head.val-1]= head
        while lst:
            prev = len(visited)
            a = lst.pop()
            if a.val not in visited:
                lst.append(a)
                for n in a.neighbors:
                    if n.val not in visited:
                        lst.append(n)
            if a.val not in visited:
                adj =[]
                for item in a.neighbors:
                    adj.append(item.val)
                k = Node(val=a.val, neighbors=adj)
                visited.append(a.val)
                if len(nodeList) < k.val:
                    for i in range(k.val):
                        nodeList.append(None)
                nodeList[k.val-1]= k
            curr = len(visited)
        for z in nodeList:
            if z:
                ne = []
                for i in z.neighbors:
                    ne.append(nodeList[i-1])
                z.neighbors = ne
        return head
            
