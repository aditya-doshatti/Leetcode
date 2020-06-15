'''
787. Cheapest Flights Within K Stops
Medium

There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Example 1:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation: 
The graph looks like this:

The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.

https://leetcode.com/problems/cheapest-flights-within-k-stops/
'''
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = defaultdict(list)
        for s, d, w in flights:
            graph[s].append((d, w))
        distances = [float("inf") for _ in range(n)]
        current_stops = [float("inf") for _ in range(n)]
        distances[src], current_stops[src] = 0, 0
        minHeap = [(0, 0, src)]     
        while minHeap:
            cost, stops, node = heapq.heappop(minHeap)
            if node == dst:
                return cost
            if stops == K + 1:
                continue
            for nei, price in graph[node]:
                dU, dV, wUV = cost, distances[nei], price
                if dU + wUV < dV:
                    distances[nei] = dU + wUV
                    heapq.heappush(minHeap, (dU + wUV, stops + 1, nei))
                elif stops < current_stops[nei]:
                    current_stops[nei] = stops
                    heapq.heappush(minHeap, (dU + wUV, stops + 1, nei))
        return -1 if distances[dst] == float("inf") else distances[dst]
    
        # graph = defaultdict(list)
        # q = [(src, 0, 0)]
        # min_price = float('inf')
        # for i, j, w in flights: 
        #     graph[i].append((j, w))
        # while q:
        #     city, curr, price = q.pop(0)
        #     if price <= min_price and curr <= K and city != dst:
        #         for node in graph[city]:
        #              q.append((node[0], curr + 1, price + node[1]))
        #     if city == dst:
        #         min_price = min(min_price, price)
        # return min_price if min_price != float('inf') else -1

        # graph = defaultdict(list)
        # for val in flights:
        #     graph[val[0]].append((val[1], val[2]))
        # visited = [0] * (n)
        # q = graph[src]
        # tmp, curr, finalVal = 0, 0, []
        # print(graph)
        # while curr <= K:
        #     newq = []
        #     while q:
        #         node = q.pop(0)
        #         # print(visited, node)
        #         if visited[node[0]] != 1:
        #             if node[0] == dst:
        #                 finalVal.append((node[1], curr))
        #             else:
        #                 visited[node[0]] = 1
        #                 if node[0] in graph:
        #                     for val in graph[node[0]]:
        #                         newq.append((val[0], val[1]+node[1]))
        #     q = newq
        #     curr += 1
        # finalVal.sort( key = lambda x: (x[0], x[1]))
        # print(finalVal)
        # for retVal in finalVal:
        #     if retVal[1] > K:
        #         continue
        #     else:
        #         return retVal[0]
        # return -1
