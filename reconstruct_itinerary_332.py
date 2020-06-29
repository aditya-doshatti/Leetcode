'''
332. Reconstruct Itinerary
Medium

Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
One must use all the tickets once and only once.
Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]

https://leetcode.com/problems/reconstruct-itinerary/
'''
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = defaultdict(list)
        for fro, to in tickets:
            graph[fro].append(to)
        for key in graph:
            graph[key].sort()
        stack, retVal = ["JFK"], []
        while stack:
            curr = stack[-1]
            if curr in graph and len(graph[curr]) > 0:
                stack.append(graph[curr].pop(0))
            else:
                retVal.append(stack.pop())
        return retVal[::-1]

        # graph = defaultdict(list)
        # for fro, to in tickets:
        #     graph[fro].append(to)
        # retVal = ["JFK"]
        # curr = retVal[-1]
        # while curr in graph:
        #     temp = sorted(graph[curr])
        #     retVal.append(temp.pop(0))
        #     if not temp:
        #         del(graph[curr])
        #     else:
        #         graph[curr] = temp
        #     curr = retVal[-1]
        # return retVal
